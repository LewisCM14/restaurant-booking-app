""" This module contains the admin logic for the menu app. """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Starter, Main, Dessert


@admin.register(Starter)
class StarterAdmin(SummernoteModelAdmin):
    """
    The Admin panel for the starters on the menu model.
    """
    summernote_fields = ('description')
    list_display = ('title',)


@admin.register(Main)
class MainAdmin(SummernoteModelAdmin):
    """
    The Admin panel for the mains on the menu model.
    """
    summernote_fields = ('description')
    list_display = ('title',)


@admin.register(Dessert)
class DessertAdmin(SummernoteModelAdmin):
    """
    The Admin panel for the desserts on the menu model.
    """
    summernote_fields = ('description')
    list_display = ('title',)
