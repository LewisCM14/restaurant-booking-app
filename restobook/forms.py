""" This module contains logic used in account creation. """

from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Extends from the allauth base signup form.

    Adds the custom sign up fields first and last name.
    These fields are collected for use when the user makes
    reservations.
    """

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Forename'})
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Surname'})
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
