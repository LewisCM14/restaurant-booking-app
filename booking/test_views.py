from django.test import TestCase
from .models import Booking


class TestViews(TestCase):
    """
    Contains the tests for the views.
    Located in the booking app in vies.py.
    """

    def test_get_index_page(self):
        """
        Uses Django's in-built HTTP client to get the index page URL slash.
        Asserts equal to status code 200, a successful HTTP response.

        Then uses assert Template Used to ensure the index.html page,
        plus the base.html it is extended from, is being used.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_booking_page(self):
        """
        Uses Django's in-built HTTP client to get /makebooking URL.
        Asserts equal to status code 200, a successful HTTP response.

        Then uses assert Template Used to ensure the booking.html page,
        plus the base.html it is extended from, is being used.
        """
        response = self.client.get('/makebooking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html', 'base.html')

    def test_get_amend_booking_page(self):
        """
        Uses the Booking Model import to create a reservation instance.
        Then uses Django's in-built HTTP client,
        to get /amend/reservation.id URL. Asserts equal to status code 200,
        a successful HTTP response.

        Then uses assert Template Used to ensure the booking.html page,
        plus the base.html it is extended from, is being used.
        """
        reservation = Booking.objects.create(
            lead='Test Lead',
            email='test@email.com',
            mobile='01509',
            date='JAN. 25, 2022',
            time='4:30 P.M.',
            notes='test',
            guests='2'
            )

        response = self.client.get(f'/amend/{reservation.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'amend_booking.html', 'base.html')

    def test_get_reservations_page(self):
        pass

    def test_create_booking_request(self):
        pass

    def test_cancel_booking_request(self):
        pass

    def test_amend_booking_request(self):
        pass
