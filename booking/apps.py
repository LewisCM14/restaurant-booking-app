""" This module configures the booking app. """

from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    Sets the variables needed for the booking app configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
