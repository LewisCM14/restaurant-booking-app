from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('lead', 'date', 'time', 'guests', 'status',)
    list_filter = ('date', 'time',)
    search_fields = ('lead',)
