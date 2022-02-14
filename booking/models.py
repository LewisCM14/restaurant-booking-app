from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


# A tuple to hold the status of the booking
# 0 - pending
# 1 - accepted
# 2 - declined

STATUS = ((0, "pending"), (1, "accepted"), (2, "declined"))


class Booking(models.Model):
    """
    The model for the booking app.

    Inherits the user from account sign up.
    Stores the booking: lead, email, mobile, date, time
    and how many guests for each individual booking.
    Plus any special requirement notes.

    Defaults the booking status to 'pending' using the above tuple.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lead = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    phoneNumberRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    mobile = models.CharField(validators=[phoneNumberRegex], max_length=16)
    phone_number = PhoneNumberField()  # needs wiring up proper
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    notes = models.TextField(max_length=200)
    guests = models.PositiveIntegerField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ Orders individual bookings by date in descending order. """
        ordering = ['-date']

    def __str__(self):
        """
        Returns the reservation date and time to be used as booking title.
        """
        return f'{self.date} {self.time}'


class Image(models.Model):
    """
    The model for all images used in the Booking app.

    Stores the name of the image for ease of coding.
    Also allows admins to store the URL of where the image is hosted
    on Cloudinary.
    """
    image = CloudinaryField('image')
    name = models.CharField(max_length=200, blank=False)
    url = models.CharField(max_length=200)
