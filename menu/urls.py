""" This module contains the URL patterns for the menu app. """

from django.urls import path
from . import views


urlpatterns = [
    path('starters', views.StarterList.as_view(), name='starters'),
    path('mains', views.Mains.as_view(), name='mains'),
    path('desserts', views.Desserts.as_view(), name='desserts'),
    path('drinks', views.Drinks.as_view(), name='drinks'),
]
