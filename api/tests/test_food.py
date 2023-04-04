from api.models import Food, Chef
from django.test import TestCase
import datetime

class FoodModelTestCase(TestCase):
    @classmethod 
    def setUpTestData(cls):
        Chef.objects.create(firstName="Clive", lastName="Dunphy", prizes=3, dob=datetime.date(2002, 8, 1), cnp="5252152551")
        Food.objects.create(foodName="Pizza", proteinGrams=50, sugarGrams=5, expirationDate=datetime.date(2002, 8, 1), quantity=300, chefCreator=Chef.objects.get())

    def test_string_method(self):
        food = Food.objects.get(foodName="Pizza")
        expected_string = "Pizza"
        self.assertEqual(str(food), expected_string)