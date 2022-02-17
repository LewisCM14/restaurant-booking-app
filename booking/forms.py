import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from .widget import DatePickerInput, TimePickerInput


def validate_opening_hour(value):
    """
    A custom validation function. intended for use on 'time' fields.
    Ensures the input value is between 11AM and 9PM.
    If validation is failed the custom error message is returned.
    """
    if not 11 <= int(value.hour) <= 21:
        raise ValidationError(
            'We only take reservations between 11AM & 9PM',
            params={'value': value},
        )


def validate_future_date(value):
    """
    A custom validation function. intended for use on 'date' fields.
    Ensures the input value is a future date.
    If validation is failed the custom error message is returned.

    If value is equal to current day provdes an alternate error message.
    """
    if value < datetime.date.today():
        raise ValidationError(
            'Please select a future date',
            params={'value': value},
        )

    elif value == datetime.date.today():
        raise ValidationError(
            'Please call to make same day reservations',
            params={'value': value},
        )


def validate_guest_size(value):
    """
    A custom validation function.
    intended for use on the 'guests' field of the BookingForm.
    If input integer is greater than 8,
    validation is failed and the custom error message is returned.

    Ensures input integer is also grater than 1.
    """
    if value > 8:
        raise ValidationError(
            'For reservations of more than 8 guests, please call and arrange',
            params={'value': value},
        )

    elif value < 1:
        raise ValidationError(
            'Please state how many guests will be attending',
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

    mobile = forms.CharField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile'}),
    )

    date = forms.DateField(
        label='Date of Booking',
        required=True,
        widget=DatePickerInput(),
        validators=[validate_future_date],
    )

    time = forms.TimeField(
        label='Arrival Time',
        required=True,
        widget=TimePickerInput(),
        validators=[validate_opening_hour],
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
        widget=forms.TextInput(attrs={'placeholder': 'Guests'}),
        validators=[validate_guest_size],
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
