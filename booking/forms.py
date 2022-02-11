from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Creates the BookingForm class that inherits from the base form.
    """

    lead = forms.CharField(
        label='Booking Lead',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )

    email = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    mobile = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile'})
    )

    date = forms.DateField(
        label='Date of Booking',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Date'})
    )

    time = forms.TimeField(
        label='Arrival Time',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Time'})
    )

    arrival = forms.DateTimeField(
        label='Reservation',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Reservation'}),
        input_formats=['%d/%m/%Y %H:%M']
    )

    notes = forms.CharField(
        label='Special Requirements',
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Any special requirements we should be aware of?'
        }),
        max_length=300
    )

    guests = forms.IntegerField(
        label='Number of Guests',
        required=True,
        min_value=1,
        widget=forms.TextInput(attrs={'placeholder': 'Guests'})
    )

    class Meta:
        """
        The booking form inherits from the Booking model.
        Takes the required fields needed for a user to make a new booking.
        """
        model = Booking
        fields = (
            'lead', 'email', 'mobile', 'date', 'time', 'arrival', 'notes', 'guests'
        )
