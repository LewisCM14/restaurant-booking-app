from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# A tuple to hold the status of the booking
# 0 - pending
# 1 - accepted
# 2 - declined

STATUS = ((0, "pending"), (1, "accepted"), (2, "declined"))


class Booking(models.Model):
    """
    The model for the booking app, stores the booking: lead,
    date, time and how many guests for the individual booking.
    Defaults the booking status to 'pending' using the above tuple.
    The notes allows for special requirements to be detailed.
    The slug field, generated from the email plus date & time of the booking,
    will be used to identify each unique/individual booking.

    The meta class orders each booking by reservation date in descending order.
    str returns the reservation date and time to be used as booking title.
    """
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name="table_booking")
    email = models.EmailField()  # needs to be taken from user account
    mobile = models.IntegerField(max_length=11)  # needs to be taken from user account, max length is ignored remove later
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(max_length=200)
    guests = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    # slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} {self.time}'
