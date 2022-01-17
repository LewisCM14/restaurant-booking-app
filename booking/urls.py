from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makebooking', views.booking, name='booking'),
    path('reservations', views.reservations, name='reservations'),
]
