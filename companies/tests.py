from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

class CompanyCreationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_company(self):
        url = reverse('company-list')

        data = {
            'user': self.user.id,
            'cnpj': '12345678901234',
            'corporate_name': 'Test Company Inc',
            'trade_name': 'Test Company',
            'status': 'Active'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['corporate_name'], 'Test Company Inc')
        self.assertEqual(response.data['trade_name'], 'Test Company')
        self.assertEqual(response.data['status'], 'Active')
        self.assertEqual(response.data['user'], self.user.id)
