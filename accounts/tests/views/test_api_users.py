from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from accounts.factories.user_factory import UserFactory


class ApiUserTestCase(APITestCase):
    url = '/api/v1/users/'

    def test_get_users_list_without_login(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_list_with_credentials(self):
        user = UserFactory()
        self.client.login(username=user.username, password=user.raw_password)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
