from django.shortcuts import render
from django.views import generic
from .models import Booking


# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('-date')
#     template_name = 'booking.html'
#     paginate_by = 6


def index(request):
    return render(request, 'index.html', {})


def booking(request):
    return render(request, 'booking.html', {})
