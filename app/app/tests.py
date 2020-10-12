from django.test import TestCase#Helper func for django test
from app.calc import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added"""
        self.assertEqual(add(2,8), 10)#assertion for testing with input values
        #assertEqual matches the value with == operator
