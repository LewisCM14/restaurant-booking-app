""" This module contains the views for the menu app. """

from django.views import generic
from .models import Starter, Main, Dessert


class StarterList(generic.ListView):
    """
    Class based view using generic for the Starter model
    found in models.py on the menu app.

    Renders on the starters.html template.
    """
    model = Starter
    queryset = Starter.objects.filter(display=1).order_by('title')
    template_name = 'starters.html'


class MainList(generic.ListView):
    """
    Class based view using generic for the Main model
    found in models.py on the menu app.

    Renders on the mains.html template.
    """
    model = Main
    queryset = Main.objects.filter(display=1).order_by('title')
    template_name = 'mains.html'


class DessertList(generic.ListView):
    """
    Class based view using generic for the Dessert model
    found in models.py on the menu app.

    Renders on the dessert.html template.
    """
    model = Dessert
    queryset = Dessert.objects.filter(display=1).order_by('title')
    template_name = 'desserts.html'
