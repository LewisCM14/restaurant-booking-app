""" This module contains the views for the menu app. """

from django.shortcuts import render


def menu(request):
    """
    Renders the menu page in the browser.
    """

    return render(request, 'menu.html', {})
