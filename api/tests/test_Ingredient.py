from api.models import Ingredient
from django.test import TestCase
import datetime

class IngredientModelTestCase(TestCase):
    @classmethod 
    def setUpTestData(cls):
        Ingredient.objects.create(ingredientName="salt", location="cluj", runningLow=False, expirationDate=datetime.date(2023, 8, 1), quantity=500)

    def test_string_method(self):
        ingredient = Ingredient.objects.get(ingredientName="salt")
        expected_string = "salt"
        self.assertEqual(str(ingredient), expected_string)