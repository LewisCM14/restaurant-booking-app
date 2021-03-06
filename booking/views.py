""" This module contains the views for the booking app. """

import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.db import IntegrityError
from .models import Booking, Image
from .forms import BookingForm


def index(request):
    """
    Renders the index page in the browser.
    Collects the image used for the hero space from the Image model,
    stores it within context to be used in index.html.
    """
    hero = Image.objects.get(name='hero')
    context = {
        'hero': hero,
    }
    return render(request, 'index.html', context)


def booking(request):
    """
    Uses an if/else statement to assert the user attempting
    to access the booking feature is an authenticated user,
    if not redirects to the sign in page. Otherwise
    renders the BookingForm on the booking.html template.

    On a POST request, gets the data from the BookingForm,
    places the data in an instance. Checks that the instance is valid.

    If the booking is invalid the BookingForm will not post,
    The fields remain populated with the POST data.
    Field validation is handled in the Booking model and BookingForm.

    If valid saves the form without commiting,
    The valid booking then has the authorized users ID applied to it.
    Plus their first & last name as the lead field
    and the email address registered to their account as the email field.

    A try/except statement is then used to ensure the booking
    meets the Booking models unique_booking constraint.
    If it passes the booking is saved to the database.
    The user is then redirected to the reservations page.

    If it fails the error message is returned as context
    along with the POST data and displayed to the user.

    The logic for these actions is employed via an if/else loop.
    """
    if request.user.is_authenticated:

        if request.method == 'POST':
            booking_form = BookingForm(request.POST)

            if booking_form.is_valid():
                user = request.user  # For use in logic below.
                current_booking = booking_form.save(commit=False)
                current_booking.user = user
                current_booking.lead = f'{user.first_name} {user.last_name}'
                current_booking.email = user.email

                try:
                    current_booking.save()
                except IntegrityError as error:
                    error = (
                        'You have already requested this reservation'
                    )
                    return render(request, 'booking.html', {
                        "booking_form": BookingForm(request.POST),
                        'error': error,
                    })

                return redirect(reverse("reservations"))

            else:
                return render(request, 'booking.html', {
                    "booking_form": BookingForm(request.POST)
                })

        else:
            return render(request, 'booking.html', {
                "booking_form": BookingForm()
            })

    else:
        return redirect(reverse("account_login"))


class ReservationList(generic.ListView):
    """
    Each individual booking within the Booking model,
    is now referred to as a reservation for clarity.

    Class based view that inherits from the Booking model.
    """
    model = Booking

    def sort(self, bookings):
        """
        A helper method for the ReservationsList class.

        Takes the bookings variable created in the get method.
        Each individual booking from this vairable is iterated over,
        all instances are checked to ensure the date field is a
        future date, done with the datetime.date.today method
        from the datetime package. Instances that have passed are marked false.

        The remaining reservations are marked true
        and returned back to the get method.
        """
        if bookings.date >= datetime.date.today():
            return True
        else:
            return False

    def get(self, request, *args, **kwargs):
        """
        Uses an if/else statement to assert user authentication,
        if failed redirects to the login page.

        If passes uses the inbuilt get method to filter reservations,
        by ones with the authorized users ID. Then calls the sort method.

        Only upcoming reservations are dispayed.
        Renders to the 'reservations.html' template.
        """
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            reservations = filter(self.sort, bookings)

            return render(
                request, 'reservations.html',
                {
                    'reservations': reservations,
                },
            )

        else:
            return redirect(reverse("account_login"))


def amend_reservation(request, reservation_id):
    """
    Uses an if/else statement to assert the user attempting
    to access the amend feature is an authenticated user,
    if not redirects to the sign in page.

    If the signed in user is authenticated
    a copy of the reservation from the Booking database is created.
    The signed in users ID is then compared to the reservations user ID.
    If not equal they are redirected to the their own reservations.

    If equal an instance of the BookingForm with the reservation ID is created.
    This instance is then returned to the amend_booking template in context.

    On a POST request, gets the amended data from the BookingForm,
    places the data in an instance. Checks that the instance is valid.

    If the instance is invalid the BookingForm is reloaded,
    It is populated with the information from the failed POST request.

    If valid, a try/except statement is then used to ensure the booking
    meets the Booking models unique_booking constraint.

    If it fails the error message is returned as context
    along with the POST data and displayed to the user.

    If it passes the existing reservation is updated with the new information
    provided in the POST request and has it's status set to 'pending' or 0
    before it is saved to the database.

    The user is then redirected to the reservations page.
    """
    if request.user.is_authenticated:
        reservation = get_object_or_404(Booking, id=reservation_id)
        current_user = request.user

        if current_user == reservation.user:
            context = {
                "mobile": reservation.mobile,
                "date": reservation.date,
                "time": reservation.time,
                "notes": reservation.notes,
                "guests": reservation.guests
            }

            if request.method == 'POST':
                booking_form = BookingForm(request.POST, instance=reservation)

                if booking_form.is_valid():
                    updated_booking = booking_form.save(commit=False)
                    updated_booking.status = 0
                    try:
                        updated_booking.save()
                    except IntegrityError as error:
                        error = (
                            'You have already requested this reservation'
                        )
                        return render(request, 'amend_booking.html', {
                            "booking_form": BookingForm(request.POST),
                            'error': error,
                        })

                    return redirect(reverse("reservations"))

                else:
                    return render(request, 'amend_booking.html', {
                        "booking_form": BookingForm(request.POST)
                    })

            else:
                return render(request, 'amend_booking.html', {
                        "booking_form": BookingForm(context)
                    })

        else:
            return redirect(reverse("reservations"))

    else:
        return redirect(reverse("account_login"))


def cancel_reservation(request, reservation_id):
    """
    Uses an if/else statement to assert the user attempting
    to access the cancel feature is an authenticated user,
    if not redirects to the sign in page.

    If the signed in user is authenticated
    a copy of the reservation from the Booking database is created.
    The signed in users ID is then compared to the reservations user ID.
    If not equal they are redirected to the sign in page.

    If equal the reservation is deleted from the database via its unique id,
    the user is then redirected back to the reservations.html page.
    """
    if request.user.is_authenticated:
        reservation = get_object_or_404(Booking, id=reservation_id)
        current_user = request.user

        if current_user == reservation.user:
            reservation.delete()
            return redirect(reverse("reservations"))

        else:
            return redirect(reverse("reservations"))

    else:
        return redirect(reverse("account_login"))
