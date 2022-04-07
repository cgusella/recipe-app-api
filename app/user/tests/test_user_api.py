from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
# rest framework test helper tools;
# APIClient is a client which we use to  make request to ou API
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
# It is a common sense that parameters which are supposed to be constant
# are written all in upper case. This is just a convention, python does
# not earn anything from that.


def create_user(**params):
    # This choice of parametrization allows us to pass the model
    # directly into the create function.
    return get_user_model().objects.create_user(**params)


# The choice to put Public in the test name is due to the fact
# that the lecturer prefers to separate the tests between public
# and private. In this way in the setups you can have part that
# autheticates and parts that doesn't authenticate.
class PublicUserApiTests(TestCase):
    # So the public API is one that is unauthenticated.
    # For instance the create_user() method does not need
    # for an authentication.
    """Tests the user API public"""
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@prova.com',
            'password': 'testpass',
            'name': 'Test name',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # 201 is the code referred to a succesfull created resource.
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        # self.assertIn('password', res.data)
        # Using functions as check_password, or what we write on assertIn
        # method allows you to check password without visualizing anythong,
        # even the encrypted version of the password.

    def test_user_exists(self):
        """Test creating a user already exixts fails"""
        payload = {
            'email': 'test@prova.com',
            'password': 'testpass',
            'name': 'Test',
        }
        create_user(**payload)
        # The double stars pass the payload dictionary as
        # 'email'='test@prova.com', etc.
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            'email': 'test@prova.com',
            'password': 'pw',
            'name': 'Test',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)
