""" This module contains the URL patterns for the menu app. """

from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.menu, name='menu'),
]
