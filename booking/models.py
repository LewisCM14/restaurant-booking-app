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

    The meta class orders each booking by reservation date in descending order.
    str returns the reservation date and time to be used as booking title.
    """
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name="table_booking")
    date = models.DateTimeField()
    time = models.DateTimeField()
    note = models.TextField(max_length=200)
    guests = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} {self.time}'
