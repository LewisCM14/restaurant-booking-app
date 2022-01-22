from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makebooking', views.booking, name='booking'),
    path('reservations', views.ReservationList.as_view(), name='reservations'),
    path('amend/<reservation_id>', views.amend_reservation, name='amend'),
    path('cancel/<reservation_id>', views.cancel_reservation, name='cancel'),
]
