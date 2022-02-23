""" This module contains the admin logic for the menu app. """

from django.contrib import admin
from .models import MenuStarter


@admin.register(MenuStarter)
class MenuStarterAdmin(admin.ModelAdmin):
    """
    The Admin panel for the starters on the menu model.
    """
    list_display = ('title',)
