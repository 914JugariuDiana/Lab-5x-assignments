from api.models import Chef
from django.test import TestCase
import datetime

class ChefModelTestCase(TestCase):
    @classmethod 
    def setUpTestData(cls):
        Chef.objects.create(firstName="Clive", lastName="Dunphy", prizes=3, dob=datetime.date(2002, 8, 1), cnp="5252152551")

    def test_string_method(self):
        chef = Chef.objects.get(firstName="Clive", lastName="Dunphy")
        expected_string = "CliveDunphy"
        self.assertEqual(str(chef), expected_string)