""" This module contains the views for the menu app. """

from django.views import generic
from .models import Starter, Main, Dessert


class Starters(generic.ListView):
    """
    Class based view using generic for the Starte model
    found in models.py on the menu app.

    Renders on the starters.html template.
    """
    model = Starter
    template_name = 'starters.html'


class Mains(generic.ListView):
    """
    Class based view using generic for the Main model
    found in models.py on the menu app.

    Renders on the mains.html template.
    """
    model = Main
    template_name = 'mains.html'


class Desserts(generic.ListView):
    """
    Class based view using generic for the Dessert model
    found in models.py on the menu app.

    Renders on the dessert.html template.
    """
    model = Dessert
    template_name = 'desserts.html'