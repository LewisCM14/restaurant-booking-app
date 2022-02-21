# """ This module contains the tests for admin.py in the booking directory. """

# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Booking


# class TestAdmin(TestCase):
#     """
#     Contains the tests for the admin methods.
#     Located in the booking app in admin.py.
#     """

#     def test_admin_can_manage_booking_status(self):
#         """"""
#         test_user = User.objects.create(
#             username='Test',
#             password='Password',
#             email='test@email.com'
#         )

#         reservation = Booking.objects.create(
#             user=test_user,
#             lead='Test Lead',
#             email='test@email.com',
#             mobile='01509',
#             date='2022-01-25',
#             time='4:30 P.M.',
#             notes='test',
#             guests='2'
#         )
