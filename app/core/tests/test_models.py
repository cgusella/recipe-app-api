from django.test import TestCase
from django.contrib.auth import get_user_model
# get_user_model returns the model saved in settings.AUTH_USER_MODEL.
# To see the methods that can be used with the defined User class in
# models.py see the model.User. They are inherited when the
# AUTH_USER_MODEL is setted.


class ModelTests(TestCase):

    def test_create_user_with_email_succesfull(self):
        """Test cretating a new user and email is successfull"""
        email = 'test@prova.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for a new user is normalized"""
        email = 'test@PROVA.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email arise error"""
        # assertRaises method gives passed test when the indicated
        # error is raised.
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test123'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
                'test@prova.com',
                'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
