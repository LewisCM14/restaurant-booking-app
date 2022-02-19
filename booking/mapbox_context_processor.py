""" This module contains the logic for the MapBox API to be site wide. """

from django.conf import settings


def mapbox_renderer(request):
    """
    Returns the MAPBOX_TOKEN from settings.py into a vairable,
    this variable is used in the base.html template.

    Allows for the MapBox display to be rendered site wide 
    without being returned as context in every view.
    """
    return {
       'mapbox_token': settings.MAPBOX_TOKEN
    }
