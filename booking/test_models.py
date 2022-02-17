""" This module contains the tests for models.py in the booking directory. """

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking


class TestModel(TestCase):
    """
    Contains the tests for the model.
    Located in the booking app in model.py.
    """

    def test_status_defaults_to_pending(self):
        """
        Creates a reservation instance.
        Then uses assert status is equal to 0,
        which is pending, as defined in the model file.

        This method also tests the str method of the model
        returns the corret value.
        """
        test_user = User.objects.create(
            username='Test',
            password='Password',
            email='test@email.com'
        )

        reservation = Booking.objects.create(
            user=test_user,
            lead='Test Lead',
            email='test@email.com',
            mobile='01509',
            date='2022-01-25',
            time='4:30 P.M.',
            notes='test',
            guests='2'
        )

        self.assertEqual(reservation.status, 0)
        self.assertEqual(str(reservation), '2022-01-25 4:30 P.M.')
