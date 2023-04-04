from api.views import IngredientQuantity
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Ingredient
import datetime

class IngredientQuantityViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
       numOfIngredients = 20
       for id in range(numOfIngredients):
          Ingredient.objects.create(ingredientName=f"Ingredient{id}", location=f"loc{id}", runningLow=id % 2, expirationDate=datetime.date(2023, 8, 1), quantity=id * 10)

    def test_filterIngredient(self):
       response = self.client.get("/api/filterIngredients/?quantity=100")
       if hasattr(response, 'data'):
         # The response has a 'data' attribute
         data = response.data
         print("OK")
       self.assertEqual(len(response.data), 9)