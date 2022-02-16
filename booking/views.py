from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Booking, Image
from .forms import BookingForm


def index(request):
    """
    Renders the index page in the browser.
    Collects the image used for the hero space from the DB,
    stores it within context to be used in index.html.
    """
    hero = Image.objects.get(name='hero')
    context = {
        'hero': hero
    }
    return render(request, 'index.html', context)


def booking(request):
    """
    Renders the BookingForm on the booking.html template.

    On a POST request, gets the data from the BookingForm,
    places the data in an instance. Checks that the instance is valid.
    If valid saves the form without commiting,
    The valid booking then has the authorized users id applied to it.
    The booking is then saved to the database.
    The user is then redirected to the reservations page.

    If the booking is invalid the BookingForm will not post,
    The fields remain populated with the POST data.
    Field validation is handled in the Booking model and BookingForm.

    The logic for these actions is employed via a if/else loop.
    """
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            current_booking = booking_form.save(commit=False)
            current_booking.user = request.user
            current_booking.save()
            return redirect(reverse("reservations"))

        else:
            return render(request, 'booking.html', {
                "booking_form": BookingForm(request.POST)
            })

    else:
        return render(request, 'booking.html', {
            "booking_form": BookingForm()
        })


class ReservationList(generic.ListView):
    """
    Each individual booking within the Booking model,
    is now referred to as a reservation for clarity.

    Class based view that inherits from the Booking model.

    Uses the inbuilt get method to filter reservations,
    so only ones made by the authorized user are dispayed,
    orders them by date asscending.

    Renders to the 'reservations.html' template.
    """
    model = Booking

    def get(self, request, *args, **kwargs):

        reservations = Booking.objects.filter(user=request.user)

        return render(
            request, 'reservations.html',
            {
                'reservations': reservations,
            },
        )


def amend_reservation(request, reservation_id):
    """
    Creates a copy of the reservation from the Booking Model database.
    Then creates an instance of the BookingForm with the reservation id.
    This instance is then returned to the amend_booking template in context.

    On a POST request, gets the amended data from the BookingForm,
    places the data in an instance. Checks that the instance is valid.
    If valid, the reservation is updated with the new information
    provided in the POST request and saved to the database.
    The user is then redirected to the reservations page.

    If the booking is invalid the BookingForm is reloaded,
    It is populated with the information 
    from the failed POST request.
    """
    reservation = get_object_or_404(Booking, id=reservation_id)
    context = {
        "lead": reservation.lead,
        "email": reservation.email,
        "mobile": reservation.mobile,
        "date": reservation.date,
        "time": reservation.time,
        "notes": reservation.notes,
        "guests": reservation.guests
    }

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=reservation)

        if booking_form.is_valid():
            booking_form.save()
            return redirect(reverse("reservations"))
        
        else:
            return render(request, 'amend_booking.html', {
                "booking_form": BookingForm(request.POST)
            })

    else:
        return render(request, 'amend_booking.html', {
                "booking_form": BookingForm(context)
            })


def cancel_reservation(request, reservation_id):
    """
    Delete the reservation via its unique id from the database.
    """
    reservation = get_object_or_404(Booking, id=reservation_id)
    reservation.delete()
    return redirect(reverse("reservations"))
