from django.contrib import admin
from .models import Booking, Image


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Allows admins a quick overview of all bookings,
    with the ability to filter by date and time for a precise overview.
    intended for use when seating walk-in customers on a given day or
    making business decsions. Also allows for search by booking lead.

    Containts methods to accept or decline the bookings within the dropdown.
    """
    list_display = ('lead', 'date', 'time', 'guests', 'status',)
    list_filter = ('date', 'time',)
    search_fields = ('lead',)
    actions = ['accept_booking', 'decline_booking']

    def accept_booking(self, request, queryset):
        """
        Allows bookings to be accepted from the dropdown menu in admin.
        """
        queryset.update(status=1)

    def decline_booking(self, request, queryset):
        """
        Allows bookings to be declined from the dropdown menu in admin.
        """
        queryset.update(status=2)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('name',)
