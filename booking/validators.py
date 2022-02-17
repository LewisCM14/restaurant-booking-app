import datetime
from django.core.exceptions import ValidationError


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