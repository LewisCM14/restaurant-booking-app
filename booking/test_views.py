# """ This module contains the tests for views.py in the booking directory. """

# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Booking, Image


# class TestViews(TestCase):
#     """
#     Contains the tests for the views.
#     Located in the booking app in views.py.
#     """

#     def setUp(self):
#         """
#         Sets up an instance within the Booking model database
#         for use when testing. Creates a User stored in test_user.
#         Then creates an instance using the Booking model with this user.

#         Then creates a second User stored in alt_user. This user is
#         for testing the redirect responses of certain views.

#         Also sets up the hero img used on the index page with the Image model.
#         """
#         test_user = User.objects.create_user(
#             username='John',
#             first_name='John',
#             last_name='Doe',
#             password='Password',
#             email='johndoe@email.com',
#         )

#         Booking.objects.create(
#             user=test_user,
#             lead='John Doe',
#             email='johndoe@email.com',
#             mobile='1509507006',
#             date='2022-01-25',
#             time='4:30 P.M.',
#             notes='none',
#             guests='2',
#         )

#         alt_user = User.objects.create_user(
#             username='Jane',
#             first_name='Jane',
#             last_name='Doe',
#             password='Password',
#             email='janedoe@email.com',
#         )

#         Image.objects.create(
#             image='ycvivnzimwll8gsswsqj',
#             name='hero',
#             url='https://res.cloudinary.com/lewiscm/image/upload/v1644361126/q3d3inlmmrfdk8onwc3t.jpg',
#         )

#     def login(self):
#         """
#         Logs into the user stored in the test_user variable.
#         Created in the setUp method.
#         Called in the below tests to pass user authentication conditions.
#         """
#         self.client.login(
#             username='John',
#             password='Password',
#             email='johndoe@email.com'
#         )

#     def test_get_index_page(self):
#         """
#         Uses Django's in-built HTTP client to get the index page URL slash.
#         Asserts equal to status code 200, a successful HTTP response.

#         Then uses assert Template Used to ensure the index.html page,
#         plus the base.html it is extended from, is being used.
#         """
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html', 'base.html')

#     def test_get_booking_page(self):
#         """
#         Calls the login method,
#         passing user authentication conditions on the booking view.

#         Uses Django's in-built HTTP client to get /makebooking URL.
#         Asserts equal to status code 200, a successful HTTP response.

#         Then uses assert Template Used to ensure the booking.html page,
#         plus the base.html it is extended from, is being used.
#         """
#         self.login()
#         response = self.client.get('/makebooking')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'booking.html', 'base.html')

#     def test_booking_redirects(self):
#         """
#         With no user signed in.
#         Uses Django's in-built HTTP client, to get /makebooking in the URL.
#         Asserts equal to status code 302, a redirect response.

#         Then asserts the redirect URL is the account login page, the correct
#         redirect location if a authorized user is not logged in.
#         """
#         response = self.client.get('/makebooking')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/accounts/login/')

#     def test_get_amend_booking_page(self):
#         """
#         Calls the login method,
#         passing user authentication conditions on the view.

#         Uses Django's in-built HTTP client,
#         to get /amend/1 in the URL. Asserts equal to status code 200,
#         a successful HTTP response.

#         There is only 1 reservation in the database, which is why the URL is,
#         /amend/1

#         Then uses assert Template Used to ensure the amend_booking.html page,
#         plus the base.html it is extended from, is being used.
#         """
#         self.login()
#         response = self.client.get('/amend/1')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'amend_booking.html', 'base.html')

#     def test_amend_booking_redirects(self):
#         """
#         With no user signed in.
#         Uses Django's in-built HTTP client, to get /amend/1 in the URL.
#         Asserts equal to status code 302, a redirect response.

#         Then asserts the redirect URL is the account login page, the correct
#         redirect location if a authorized user is not logged in.

#         Then signs into the alt_user, 'Jane Doe' created in the setUp method.
#         Uses Django's in-built HTTP client, to get /amend/1 in the URL.
#         Asserts equal to status code 302, a redirect response.

#         Then asserts the redirect URL is the reservation page, the correct
#         redirect location as /amend/1 is the URL of a reservation for
#         the test_user or 'John Doe' and not Jane.
#         """
#         response = self.client.get('/amend/1')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/accounts/login/')

#         self.client.login(
#             username='Jane',
#             password='Password',
#             email='janedoe@email.com'
#         )

#         response = self.client.get('/amend/1')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/reservations')

#     def test_get_reservations_page(self):
#         """
#         Calls the login method,
#         passing user authentication conditions on the view.

#         Uses Django's in-built HTTP client to get /reservations URL.
#         Asserts equal to status code 200, a successful HTTP response.

#         Then uses assert Template Used to ensure the reservations.html page,
#         plus the base.html it is extended from, is being used.
#         """
#         self.login()
#         response = self.client.get('/reservations')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'reservations.html', 'base.html')

#     def test_reservations_redirects(self):
#         """
#         With no user signed in.
#         Uses Django's in-built HTTP client, to get /reservations in the URL.
#         Asserts equal to status code 302, a redirect response.

#         Then asserts the redirect URL is the account login page, the correct
#         redirect location if a authorized user is not logged in.
#         """
#         response = self.client.get('/reservations')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/accounts/login/')

#     def test_create_booking_request(self):
#         """
#         Uses the count method to return
#         the total number of reservations in the Booking database.
#         Then assets equal to 1,
#         as there should only be the reservation made in the setUp method.
#         """
#         count = Booking.objects.count()
#         self.assertEqual(count, 1)

#     def test_cancel_booking_request(self):
#         """
#         Calls the login method,
#         passing user authentication conditions on the view.
#         Uses Django's in-built HTTP client, to get /cancel/1 in the URL.
#         Asserts response is equal to status code 302, a redirect response.

#         This response removes the reservation created in the setUp method.
#         Then asserts the response redirects to the /reservations URL.
#         Which is the correct redirect.

#         Then filters the Booking database by ID 1.
#         asserts the length of the variable this is stored in
#         is equal to 0, meaning the reservation has been removed
#         from the database.
#         """
#         self.login()
#         response = self.client.get('/cancel/1')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/reservations')
#         existing_reservation = Booking.objects.filter(id=1)
#         self.assertEqual(len(existing_reservation), 0)

#     def test_cancel_booking_redirects(self):
#         """
#         Signs into the alt_user, 'Jane Doe' created in the setUp method.
#         Uses Django's in-built HTTP client, to get /cancel/1 in the URL.
#         Asserts equal to status code 302, a redirect response.

#         Then asserts the redirect URL is the reservation page, the correct
#         redirect location as /cancel/1 is the URL of a reservation for
#         the test_user or 'John Doe' and not Jane.

#         Then filters the Booking database by ID 1.
#         asserts the length of the variable this is stored in
#         is equal to 1, meaning the reservation hasn't been removed
#         from the database.
#         """
#         self.client.login(
#             username='Jane',
#             password='Password',
#             email='janedoe@email.com'
#         )

#         response = self.client.get('/cancel/1')
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/reservations')
#         existing_reservation = Booking.objects.filter(id=1)
#         self.assertEqual(len(existing_reservation), 1)
