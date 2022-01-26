from django.test import TestCase
from .models import Booking

class TestModel(TestCase):
    """
    Contains the tests for the model.
    Located in the booking app in model.py.
    """

    def test_status_defaults_to_pending(self):
        """
        Creates a reservation instance.
        Then uses assert equal to 0,
        which is pending, as defined in the model file.
        """
