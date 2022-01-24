from django.test import TestCase
from . forms import BookingForm


class TestBookingForm(TestCase):

    def test_lead_is_required(self):
        form = BookingForm({'lead': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('lead', form.errors.keys())
        self.assertEqual(form.errors['lead'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests'])
