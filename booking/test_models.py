""" This module contains the tests for models.py in the booking directory. """

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking


class TestModel(TestCase):
    """
    Contains the tests for the Booking model.
    Located in the booking app in model.py.
    """

    def test_status_defaults_to_pending(self):
        """
        Creates a User instance for use in testing.
        Then creates a Booking instance for this test_user.

        This instance is stored in the reservation variable.
        The status is not set.Then uses assert status is equal to 0
        which is pending, as defined in the model.py file.
        Meaning the status field of the Booking model defaults to pending.

        This method also tests that the str method of the Booking model
        returns the corret value, which is the date and time of the Booking.
        This is tested with assert equal that str(reservation) is the
        value for the date and time fields of the reservation instance.
        """
        test_user = User.objects.create(
            username='John',
            first_name='John',
            last_name='Doe',
            password='Password',
            email='johndoe@email.com'
        )

        reservation = Booking.objects.create(
            user=test_user,
            lead='John Doe',
            email='johndoe@email.com',
            mobile='1509507006',
            date='2022-01-25',
            time='4:30 P.M.',
            notes='none',
            guests='2'
        )

        self.assertEqual(reservation.status, 0)
        self.assertEqual(str(reservation), '2022-01-25 4:30 P.M.')
