from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Company


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


class CompanyListTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpassword123')
        self.user2 = User.objects.create_user(username='user2', password='testpassword123')

        self.token_user1 = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user1.key)

        Company.objects.create(user=self.user1, cnpj="11111111111111", corporate_name="Company One", trade_name="C1")
        Company.objects.create(user=self.user1, cnpj="22222222222222", corporate_name="Company Two", trade_name="C2")

        Company.objects.create(user=self.user2, cnpj="33333333333333", corporate_name="Company Three", trade_name="C3")

    def test_list_companies_for_logged_in_user(self):
        url = reverse('company-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        companies_user1_ids = {company['id'] for company in response.data}
        expected_ids = set(Company.objects.filter(user=self.user1).values_list('id', flat=True))
        self.assertEqual(companies_user1_ids, expected_ids)