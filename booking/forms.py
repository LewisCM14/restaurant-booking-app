from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """
    Creates the BookingForm class that inherits from the base form.
    """
    class Meta:
        """
        The booking form inherits from the Booking model.
        Takes the required fields needed for a user to make a new booking.
        """
        model = Booking
        fields = (
            'lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests',
        )
