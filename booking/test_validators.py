""" This module tests the functions in validators.py in the booking app. """

from django.test import TestCase
from django.core.exceptions import ValidationError
from . import validators


class TestValidators(TestCase):
    """
    Contains the tests for the validators used in the BookingForm.
    Located in the booking directory in validators.py.
    """

    # def test_opening_hours_validates(self):
    #     """

    #     """

    # def test_future_date_validates(self):
    #     """

    #     """

    # def test_open_day_validates(self):
    #     """

    #     """

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
