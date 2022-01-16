from django.shortcuts import render
#  from django.views import generic
from .models import Booking
from .forms import BookingForm


# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('-date')
#     template_name = 'booking.html'
#     paginate_by = 6


def index(request):
    return render(request, 'index.html', {})


def booking(request):

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
            print("form is valid")
            booking_form.save()
        else:
            print("form invalid")
            print(booking_form.errors)

        return render(request, 'index.html', {})  # temp

    else:
        print("form is NOT valid")
        return render(request, 'booking.html', {
            "booking_form": BookingForm()
        })

    return render(request, 'booking.html', {
        "booking_form": BookingForm()
    })


# def createbooking(request):
#     """
#     On a POST request, gets the data from the form and places in an instance.
#     Checks that the instance is valid and if so saves to the database.
#     """
    
