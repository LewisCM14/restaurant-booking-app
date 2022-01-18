from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm


def index(request):
    """ Renders the index page in the browser """
    return render(request, 'index.html', {})


def booking(request):
    """
    Renders the BookingForm in the browser.

    On a POST request, gets the data from the form and places in an instance.
    Checks that the instance is valid and if so saves to the database,
    then redirects to the reservations page. If form is invalid, reloads
    booking page.
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
            booking_form.save()

        return render(request, 'reservations.html', {})

    else:
        return render(request, 'booking.html', {
            "booking_form": BookingForm()
        })  # alter to booking page that says previous was invalid

    return render(request, 'booking.html', {
        "booking_form": BookingForm()
    })


# def reservations(request):
#     """ Renders the reservations page in the browser """
#     return render(request, 'reservations.html', {})


class ReservationList(generic.ListView):
    """
    Class based view to display the reservations of a user.
    Inherits from the Booking model.
    Filters bookings so only ones made by the singed in user are dispayed,
    orders them by date asscending.
    Renders to the 'reservations.html' template.
    Paginates the bookings to 6 per page.
    """
    model = Booking
    # queryset = needs to filter only bookings of logged in user
    template_name = 'reservations.html'
    paginate_by = 6
