from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test whether the user is successfully created with email"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))#check_password is helper
        #fn of get_user_model.this is used since pwd is hashed

    def test_new_user_email_normalized(self):
        """Test whether the email is normalized for new user created"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email,password='test')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test email is being given for user creation. anyline after with
        should raise value error since no email is passed for user creation"""

        with self.assertRaises(ValueError):
            get_user_model.objects.create_user(None, 'testpwd')

    def test_create_new_superuser(self):
        """Test whether the user created is superuser"""
        user = get_user_model.objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
