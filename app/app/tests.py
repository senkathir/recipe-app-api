from django.test import TestCase#Helper func for django test
from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added"""
        self.assertEqual(add(2,8), 10)#assertion for testing with input values
        #assertEqual matches the value with == operator

    def test_subtract(self):
        """Test the subtract result"""
        self.assertEqual(subtract(5,14), 9)
