""" This module configures the menu app. """

from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Sets the variables needed for the menu app configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
