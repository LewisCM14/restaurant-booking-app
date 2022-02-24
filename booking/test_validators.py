""" This module tests the functions in validators.py in the booking app. """

import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from . import validators


class TestValidators(TestCase):
    """
    Contains the tests for the validators used in the BookingForm.
    Located in the booking directory in validators.py.
    """
    def test_future_date_validates(self):
        """
        Using the datetime libray, stores todays date in a variable.
        Then adds one day to this variable to collect tomorrows date.
        Removes one day from the today variable to collect yesterdays date.

        Using the 'future' variable asserts no errors are raised when
        passed to the validate_future_date method.

        Using the 'today' and 'yesterday' variables asserts ValidationErrors
        are raised when passed to the validate_future_date method
        """
        today = datetime.date.today()
        future = today + datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=1)

        self.assertIsNone(validators.validate_future_date(future))

        with self.assertRaises(ValidationError):
            validators.validate_future_date(today)

        with self.assertRaises(ValidationError):
            validators.validate_future_date(yesterday)

    def test_guest_size_validates(self):
        """
        Creates a list of the number of guests that pass validation.
        Iterates over this list and asserts that no errors are raised
        when passing the integer value to the validate_guest_size method.

        Then asserts that the integers 0 or 9 raise a validation error
        when passed to the validate_guest_size method.
        """
        guests = [1, 2, 3, 4, 5, 6, 7, 8]

        for num in guests:
            self.assertIsNone(validators.validate_guest_size(num))

        with self.assertRaises(ValidationError):
            validators.validate_guest_size(0)

        with self.assertRaises(ValidationError):
            validators.validate_guest_size(9)
