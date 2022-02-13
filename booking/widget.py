from django import forms


class DatePickerInput(forms.DateInput):
    """
    Defines the date picker widget used in the BookingForm.
    The BookingForm is found in forms.py
    """
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    """
    Defines the time picker widget used in the BookingForm.
    The BookingForm is found in forms.py
    """
    input_type = 'time'
