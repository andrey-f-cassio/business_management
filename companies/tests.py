from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse('user-register')
        data = {
            'first_name': 'jackie',
            'last_name': 'Sparrow',
            'email': 'jackiesparrow@example.com',
            'password': '123456'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jackiesparrow@example.com', email='jackiesparrow@example.com',
                                             password='123456')

    def test_user_login(self):
        url = reverse('user-login')
        data = {
            'email': 'jackiesparrow@example.com',
            'password': '123456'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

