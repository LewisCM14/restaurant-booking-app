from django.test import TestCase
from . forms import BookingForm


class TestBookingForm(TestCase):
    """
    Contains the tests for the BookingForm.
    Located in the booking app in forms.py.
    """

    def test_lead_is_required(self):
        """
        Creates an instance of the BookingForm with the lead field empty.
        Then uses assert false on form.is_valid,
        this returns false, confirming the lead field is required.

        Also sends back a dictionary of fields on which there were errors
        and the Associated error messages. Then uses assert in,
        to confirm theirs a lead key in the dictionairy of form errors.

        Then uses assert equal to check whether the error message
        on the lead field is 'This field is required.'
        """
        form = BookingForm({'lead': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('lead', form.errors.keys())
        self.assertEqual(form.errors['lead'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Follows same logic for test_lead_is_required
        """
        form = BookingForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_mobile_is_required(self):
        """
        Follows same logic for test_lead_is_required
        """
        form = BookingForm({'mobile': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('mobile', form.errors.keys())
        self.assertEqual(form.errors['mobile'][0], 'This field is required.')

    def test_date_is_required(self):
        """
        Follows same logic for test_lead_is_required
        """
        form = BookingForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_time_is_required(self):
        """
        Follows same logic for test_lead_is_required
        """
        form = BookingForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_guests_is_required(self):
        """
        Follows same logic for test_lead_is_required
        """
        form = BookingForm({'guests': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors.keys())
        self.assertEqual(form.errors['guests'][0], 'This field is required.')

    # def test_notes_is_not_required(self):
    #     """
    #     Creates an instance of the BookingForm,
    #     with only the 'notes' field blank.
    #     Then uses assert true to make sure the form is valid.
    #     This confirms that even with notes left blank, the form is still valid,
    #     meaning notes isn't required on the BookingForm.
    #     """
    #     form = BookingForm({
    #         'lead': 'Booking Lead',
    #         'email': 'test@email.com',
    #         'mobile': '01509',
    #         'date': '2022-01-25',
    #         'time': '4:30 P.M.',
    #         'notes': '',
    #         'guests': '2'
    #     })
    #     self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Creates an empty instance of the BookingForm,
        then use assert equal to check whether the form.meta.fields attribute
        is equal to the fields specified in forms.py.
        """
        form = BookingForm()
        self.assertEqual(form.Meta.fields, (
            'lead', 'email', 'mobile', 'date', 'time', 'notes', 'guests'
            ))
