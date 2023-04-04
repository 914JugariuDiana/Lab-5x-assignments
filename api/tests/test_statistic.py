from api.views import IngredientQuantity
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Chef, Food
import datetime

class IngredientQuantityViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        numOfChefs = 15
        numOfFoods = 10
        for id in range(numOfChefs):
            Chef.objects.create(firstName=f"first{id}", lastName=f"last{id}", prizes=id % 5, dob=datetime.date(1990, 8, 1), cnp=f"01234567891{id}")
          
        for idf in range(numOfFoods):
            Food.objects.create(foodName=f"food{idf}", proteinGrams=idf * 7.5, sugarGrams=idf * 0.3, expirationDate=datetime.date(2002, 8, 1), quantity=idf * 100, chefCreator=(Chef.objects.get(firstName = f"first{id // 5 * 12 % 15}")))
    
    def test_filterIngredient(self):
       response = self.client.get("/api/orderChefs/")
       second = response.data[0]['avgQuantity']
       for i in range(1, len(response.data)):
            first = second
            second = response.data[i]['avgQuantity']
            if (first != None and second != None):
                self.assertEqual(second, first)