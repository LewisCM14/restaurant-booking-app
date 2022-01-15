from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Extends from allauth base signup form,
    adds custom sign up fields.
    """

    full_name = forms.CharField(max_length=50, label='Full Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.save()
        return user
