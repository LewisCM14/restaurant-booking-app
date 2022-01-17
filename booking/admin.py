from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Allows admins a quick overview of all bookings,
    with the ability to filter by date and time for a precise overview
    intended for use when seating walk-in customers on a given day.
    Also allows for search by booking lead.
    """
    list_display = ('lead', 'date', 'time', 'guests', 'status',)
    list_filter = ('date', 'time',)
    search_fields = ('lead',)
