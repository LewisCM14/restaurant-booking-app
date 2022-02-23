""" This module contains the views for the menu app. """

from django.views import generic
from .models import Starter


class Starters(generic.ListView):
    """
    Class based view using generic for the Starter model
    found in models.py on the menu app.

    Renders on the starters.html template.
    """
    model = Starter
    template_name = 'starters.html'
