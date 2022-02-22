# """ This module contains the tests for admin.py in the booking directory. """

# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Booking
# from .admin import BookingAdmin


# class TestAdmin(TestCase):
#     """
#     Contains the tests for the admin methods.
#     Located in the booking app in admin.py.
#     """
#     def test_admin_funcs(self):
#         """
#         Sets up an instance within the Booking model database
#         for use when testing. Creates a User stored in test_user.
#         Then creates an instance using the Booking model with this user.

#         Then creates a second User stored in alt_user. This user is
#         for testing the redirect responses of certain views.

#         Also sets up the hero img used on the index page with the Image model.
#         """
#         test_user = User.objects.create(
#             username='John',
#             first_name='John',
#             last_name='Doe',
#             password='Password',
#             email='johndoe@email.com',
#         )

#         reservation = Booking.objects.create(
#             user=test_user,
#             lead='John Doe',
#             email='johndoe@email.com',
#             mobile='1509507006',
#             date='2022-01-25',
#             time='4:30 P.M.',
#             notes='none',
#             guests='2',
#         )

#         self.assertEqual(reservation.status, 0)
#         BookingAdmin.accept_booking(self, 'POST', [reservation,])
#         self.assertEqual(reservation.status, 1)

#     # def test_admin_funcs(self):
#     #     reservation = Booking.objects.filter(id=1)
#     #     self.assertEqual(reservation.status, 0)