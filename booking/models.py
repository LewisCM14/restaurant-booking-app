""" This module contains the database models for the booking app. """

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField


# A tuple to hold the status key for the Booking model.
STATUS = ((0, "pending"), (1, "accepted"), (2, "declined"))


class Booking(models.Model):
    """
    The model for the booking app.

    Inherits the user from account sign up.
    Stores the booking: lead, email, mobile, date, time
    and how many guests for each individual booking.
    Plus any special requirement notes.

    Defaults the booking status to 'pending' using the above tuple.

    Validation for the mobile field is handled with Django's inbuilt
    RegexValidator.
    """
    # Foreign Key from the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User Info needed for Booking
    lead = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    # Contact Number for Booking & Validator
    phoneNumberRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    mobile = models.CharField(
        validators=[phoneNumberRegex], max_length=16, blank=False
        )
    # Date of Booking
    date = models.DateField(blank=False)
    # Time of Booking
    time = models.TimeField(blank=False)
    # Special Requests for Booking
    notes = models.TextField(max_length=200)
    # Number of Guests on Booking
    guests = models.PositiveIntegerField(blank=False)
    # Booking Status - status updates handled in admin
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Orders individual bookings by date in descending order.

        Uses Django's inbuilt UniqueConstraint method to ensure
        a user cannot make a duplicate booking for the same
        date & time as one they already have stored in the Booking database.

        If a double booking is made, the errorr raised is handled in the
        relevant views in the booking directory under views.py.
        """
        ordering = ['-date']

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'date', 'time'], name='unique_booking'
            ), ]

    def __str__(self):
        """
        Returns the booking date and time to be used as the booking title.
        Defining this method is reccomended by Django.
        """
        return f'{self.date} {self.time}'


class Image(models.Model):
    """
    The model for all images used in the restobook project.

    Stores the name of the image for ease of coding.
    Also allows admins to store the URL of where the image is hosted
    on Cloudinary.
    """
    image = CloudinaryField('image')
    name = models.CharField(max_length=200, blank=False)
    url = models.CharField(max_length=200)
