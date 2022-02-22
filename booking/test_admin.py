""" This module contains the tests for admin.py in the booking directory. """

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking
from .admin import BookingAdmin


class TestAdmin(TestCase):
    """
    Contains the tests for the admin methods.
    Located in the booking app in admin.py.
    """
    def test_admin_methods(self):
        """
        Sets up a User instance for use when testing.
        Stored in test_user, then uses them to create two reservations
        using the Booking model.

        Asserts both reservations default to pending.

        Then calls the accept_booking method from the BookingAdmin class.
        asserts this sets reservation1 status to 1 which is 'accepted'.

        Then calls the decline_booking method from the BookingAdmin class.
        asserts this sets reservation1 status to 2 which is 'declined'.

        Then follows the same logic on both reservations to ensure multiple
        instances can be accepted or declined at once by the admin.
        """
        test_user = User.objects.create(
            username='John',
            first_name='John',
            last_name='Doe',
            password='Password',
            email='johndoe@email.com',
        )

        reservation1 = Booking.objects.create(
            user=test_user,
            lead='John Doe',
            email='johndoe@email.com',
            mobile='1509507006',
            date='2022-01-25',
            time='11:00:00',
            notes='none',
            guests='2',
        )

        reservation2 = Booking.objects.create(
            user=test_user,
            lead='John Doe',
            email='johndoe@email.com',
            mobile='1509507006',
            date='2022-01-26',
            time='11:00:00',
            notes='none',
            guests='2',
        )

        # Asserts both start with status pending.
        self.assertEqual(reservation1.status, 0)
        self.assertEqual(reservation2.status, 0)

        # Passes the 1st reservation to the method, asserts status accepted.
        BookingAdmin.accept_booking(self, 'POST', [reservation1, ])
        self.assertEqual(reservation1.status, 1)

        # Passes the 1st reservation to the method, asserts status declined.
        BookingAdmin.decline_booking(self, 'POST', [reservation1, ])
        self.assertEqual(reservation1.status, 2)

        # Passes both reservations to the method, asserts status accepted.
        BookingAdmin.accept_booking(
            self, 'POST', [reservation1, reservation2, ]
        )
        self.assertEqual(reservation1.status, 1)
        self.assertEqual(reservation2.status, 1)

        # Passes both reservations to the method, asserts status declined.
        BookingAdmin.decline_booking(
            self, 'POST', [reservation1, reservation2, ]
        )
        self.assertEqual(reservation1.status, 2)
        self.assertEqual(reservation2.status, 2)
