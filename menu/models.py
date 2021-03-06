""" This module contains the database model for the menu app. """

from django.db import models
from cloudinary.models import CloudinaryField

# A tuple for controlling if an item is on the menu or not.
DISPLAY = ((0, "Off"), (1, "On"))


class Starter(models.Model):
    """
    The model for the starters on the menu app.

    Stores the title of each item plus a brief description
    and the price. An image for the item can be stored as a
    cloudinary field. This is currently intended for future
    features.

    The title must be unique to prevent the same item being
    added multiple times. The price field uses a decimal field
    to ensure a valid price format can be added.

    The display field uses the DISPLAY tuple to control if an
    item is on the menu or not. Also used for the queryset in the view.
    """
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = CloudinaryField('image', blank=True)
    display = models.IntegerField(choices=DISPLAY)

    class Meta:
        """
        Orders the starter items alphabetically by title.
        """
        ordering = ['title']

    def __str__(self):
        """
        Returns the starter items title as a string.
        Defining this method is reccomended by Django.
        """
        return f'{self.title}'


class Main(models.Model):
    """
    The model for the mains on the menu app.

    Stores the title of each item plus a brief description
    and the price. An image for the item can be stored as a
    cloudinary field. This is currently intended for future
    features.

    The title must be unique to prevent the same item being
    added multiple times. The price field uses a decimal field
    to ensure a valid price format can be added.

    The display field uses the DISPLAY tuple to control if an
    item is on the menu or not. Also used for the queryset in the view.
    """
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = CloudinaryField('image', blank=True)
    display = models.IntegerField(choices=DISPLAY)

    class Meta:
        """
        Orders the mains items alphabetically by title.
        """
        ordering = ['title']

    def __str__(self):
        """
        Returns the mains item title as a string.
        Defining this method is reccomended by Django.
        """
        return f'{self.title}'


class Dessert(models.Model):
    """
    The model for the desserts on the menu app.

    Stores the title of each item plus a brief description
    and the price. An image for the item can be stored as a
    cloudinary field. This is currently intended for future
    features.

    The title must be unique to prevent the same item being
    added multiple times. The price field uses a decimal field
    to ensure a valid price format can be added.

    The display field uses the DISPLAY tuple to control if an
    item is on the menu or not. Also used for the queryset in the view.
    """
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = CloudinaryField('image', blank=True)
    display = models.IntegerField(choices=DISPLAY)

    class Meta:
        """
        Orders the dessert items alphabetically by title.
        """
        ordering = ['title']

    def __str__(self):
        """
        Returns the dessert items title as a string.
        Defining this method is reccomended by Django.
        """
        return f'{self.title}'
