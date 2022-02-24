""" This module contains the tests for models.py in the booking directory. """

from django.test import TestCase
from .models import Starter, Main, Dessert


class TestModel(TestCase):
    """
    Contains the tests for the Menu model.
    Located in the menu app in model.py.
    """

    def test_starter_string_method_returns_title(self):
        """
        Using the Starter model creates an object
        stored in the variable starter. Then calls the str method
        of this model and asserts the value is equal to
        the title of the starter variable.
        """
        starter = Starter.objects.create(
            title='starter',
            description="description",
            price='1.00',
            display='1',
        )

        self.assertEqual(str(starter), 'starter')

    def test_main_string_method_returns_title(self):
        """
        Using the Main model creates an object
        stored in the variable main. Then calls the str method
        of this model and asserts the value is equal to
        the title of the main variable.
        """
        main = Main.objects.create(
            title='main',
            description="description",
            price='1.00',
            display='1',
        )

        self.assertEqual(str(main), 'main')

    def test_dessert_string_method_returns_title(self):
        """
        Using the Dessert model creates an object
        stored in the variable dessert. Then calls the str method
        of this model and asserts the value is equal to
        the title of the dessert variable.
        """
        dessert = Dessert.objects.create(
            title='dessert',
            description="description",
            price='1.00',
            display='1',
        )

        self.assertEqual(str(dessert), 'dessert')
