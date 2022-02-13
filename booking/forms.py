from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from .widget import DatePickerInput, TimePickerInput


def validate_opening_hour(value):
    """
    Validates the time field is within opening hours.
    """
    if not 11 < int(value.hour) < 21:  # do i need value.hour or just value
        print(value)
        raise ValidationError(
            'We only take reservations on the hour between 11AM & 9PM',
            params={'value': value},
        )


class BookingForm(forms.ModelForm):
    """
    Creates the BookingForm class that inherits from the base form.
    """

    lead = forms.CharField(
        label='Booking Lead',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'}),
    )

    email = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )

    mobile = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile'}),
    )

    date = forms.DateField(
        label='Date of Booking',
        required=True,
        widget=DatePickerInput(),
    )

    time = forms.TimeField(
        label='Arrival Time',
        required=True,
        widget=TimePickerInput(),
        validators=[validate_opening_hour]
    )

    notes = forms.CharField(
        label='Special Requirements',
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Any special requirements we should be aware of?'
        }),
        max_length=300,
    )

    guests = forms.IntegerField(
        label='Number of Guests',
        required=True,
        min_value=1,
        widget=forms.TextInput(attrs={'placeholder': 'Guests'}),
    )

    class Meta:
        """
        The booking form inherits from the Booking model.
        Takes the required fields needed for a user to make a new booking.

        Defines the widgets for the date and time fields.
        """
        model = Booking
        fields = (
            'lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests'
        )

        widgets = {
            'date': DatePickerInput,
            'time': TimePickerInput,
        }
