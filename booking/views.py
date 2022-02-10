from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Booking, Image
from .forms import BookingForm


def index(request):
    """ Renders the index page in the browser. """
    # images = Image.objects.all()
    # context = {
    #     'images': images
    # }
    return render(request, 'index.html', {})


def booking(request):
    """
    Renders the BookingForm on the booking.html template.

    On a POST request, gets the data from the BookingForm,
    places the data in an instance. Checks that the instance is valid.
    If valid saves the form without commiting,
    The valid booking then has the authorized users id applied to it.
    The booking is then saved to the database.
    The user is then redirected to the reservations page.

    If the booking is invalid the BookingForm is reloaded.

    The logic for these actions is employed via a if/else loop.
    """
    if request.method == 'POST':
        form_data = {
            "lead": request.POST.get('lead'),
            "email": request.POST.get('email'),
            "mobile": request.POST.get('mobile'),
            "date": request.POST.get('date'),
            "time": request.POST.get('time'),
            "notes": request.POST.get('notes'),
            "guests": request.POST.get('guests')
        }

        booking_form = BookingForm(form_data)

        if booking_form.is_valid():
            current_booking = booking_form.save(commit=False)
            current_booking.user = request.user
            current_booking.save()
            return redirect(reverse("reservations"))

        else:
            return render(request, 'booking.html', {
                "booking_form": BookingForm()
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
    Paginates the bookings to 6 per page.

    Uses the inbuilt get method to filter reservations,
    so only ones made by the authorized user are dispayed,
    orders them by date asscending.

    Renders to the 'reservations.html' template.
    """
    model = Booking
    paginate_by = 6

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
    If valid, the previous reservation is deleted from the database.
    The new reservation is then saved without commiting,
    The instance then has the authorized users id applied to it.
    The reservation is then saved to the database.
    The user is then redirected to the reservations page.

    If the booking is invalid the BookingForm is reloaded,
    It is populated with the context instance.
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
        form_data = {
            "lead": request.POST.get('lead'),
            "email": request.POST.get('email'),
            "mobile": request.POST.get('mobile'),
            "date": request.POST.get('date'),
            "time": request.POST.get('time'),
            "notes": request.POST.get('notes'),
            "guests": request.POST.get('guests')
        }

        booking_form = BookingForm(form_data)

        if booking_form.is_valid():
            reservation.delete()
            current_booking = booking_form.save(commit=False)
            current_booking.user = request.user
            current_booking.save()
            return redirect(reverse("reservations"))

        else:
            return render(request, 'amend_booking.html', {
                "booking_form": BookingForm(context)
            })

    else:
        return render(request, 'amend_booking.html', {
                "booking_form": BookingForm(context)
            })


def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Booking, id=reservation_id)
    reservation.delete()
    return redirect(reverse("reservations"))
