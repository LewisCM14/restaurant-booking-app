""" This module contains the admin logic for the menu app. """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Starter


@admin.register(Starter)
class StarterAdmin(SummernoteModelAdmin):
    """
    The Admin panel for the starters on the menu model.
    """
    summernote_fields = ('description')
    list_display = ('title',)
