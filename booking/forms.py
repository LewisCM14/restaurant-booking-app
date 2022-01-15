from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """
    Create our BookingForm class that inherits from the base form.
    """
    class Meta:
        """
        Telling our booking form what model to use,
        then which fields we want displayed on our form.
        trailing comma means python reads as tuple, not string
        """
        model = Booking
        fields = ('lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests',)
