from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-date')
    template_name = 'booking.html'


def index(request):
    return render(request, 'index.html', {})
