from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """
    Creates the BookingForm class that inherits from the base form.
    """

    lead = forms.CharField(
        label='Name of Booking Lead',
        required=True,
    )

    email = forms.EmailField(
        label='Email Address',
        required=True,
    )

    mobile = forms.IntegerField(
        label='Best Contact Number (Mobile)',
        required=True,
    )

    date = forms.DateField(
        label='Date of Booking',
        required=True,
    )

    time = forms.TimeField(
        label='Arrival Time',
        required=True,
    )

    notes = forms.CharField(
        label='Special Requirements',
        required=False,
        widget=forms.Textarea,
        max_length=300
    )

    guests = forms.IntegerField(
        label='Number of Guests',
        required=True,
        min_value=1
    )

    class Meta:
        """
        The booking form inherits from the Booking model.
        Takes the required fields needed for a user to make a new booking.
        """
        model = Booking
        fields = (
            'lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests'
        )
