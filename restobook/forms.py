from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Extends from allauth base signup form,
    adds custom sign up fields.
    """

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    mobile_number = forms.CharField(max_length=11, label='Mobile Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user
