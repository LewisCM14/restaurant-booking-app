from django.test import TestCase
from .models import Booking
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Contains the tests for the views.
    Located in the booking app in views.py.
    """

    def setUp(self):
        """
        Creates a reservation instance using the Booking model,
        for use within the test case.
        """
        test_user = User.objects.create(
            username='Test',
            password='Password',
            email='test@email.com'
        )

        Booking.objects.create(
            user=test_user,
            lead='Test Lead',
            email='test@email.com',
            mobile='01509',
            date='2022-01-25',
            time='4:30 P.M.',
            notes='test',
            guests='2'
        )

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
        Uses Django's in-built HTTP client,
        to get /amend/1 in the URL. Asserts equal to status code 200,
        a successful HTTP response.

        There is only 1 reservation in the database, which is why the URL is,
        /amend/1

        Then uses assert Template Used to ensure the amend_booking.html page,
        plus the base.html it is extended from, is being used.
        """
        response = self.client.get('/amend/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'amend_booking.html', 'base.html')

    # def test_get_reservations_page(self):
    #     """
    #     Uses Django's in-built HTTP client to get /reservations URL.
    #     Asserts equal to status code 200, a successful HTTP response.

    #     Then uses assert Template Used to ensure the reservations.html page,
    #     plus the base.html it is extended from, is being used.
    #     """
    #     response = self.client.get('/reservations')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'reservations.html', 'base.html')

    def test_create_booking_request(self):
        """
        Uses the count method to return
        the total number of reservations in the Booking database.
        Then assets equal to 1,
        as there should only be the reservation made in the setUp method.
        """
        count = Booking.objects.count()
        self.assertEqual(count, 1)

    def test_cancel_booking_request(self):
        """
        Removes the reservation created in the setUp method
        using the cancel URL with id 1.

        Then filters the Booking database by this id.
        asserts the length of the variable this is stored in
        is equal to 0, meaning the reservation has been removed
        from the database.
        """

        self.client.get('/cancel/1')
        existing_reservation = Booking.objects.filter(id=1)
        self.assertEqual(len(existing_reservation), 0)
