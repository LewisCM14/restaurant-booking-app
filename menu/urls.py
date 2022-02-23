""" This module contains the URL patterns for the menu app. """

from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.Starters.as_view(), name='starters'),
    # path('menu', views.Mains.as_view(), name='mains'),
    # path('menu', views.Desserts.as_view(), name='desserts'),
    # path('menu', views.Drinks.as_view(), name='drinks'),
]
