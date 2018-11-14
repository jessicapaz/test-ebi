import json

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User


class SellerTestCase(APITestCase):
    url = '/seller/'

    def setUp(self):
        self.username = "jessicapaz"
        self.password = "test"
        self.user = User.objects.create_user(self.username, self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_seller(self):
        data = {
          "name": "Jessica",
          "rg": "456446",
          "cpf": "465468865",
          "phone": "45465464",
          "seller": {
            "salary": 6554.6
            }
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(json.loads(response.content), data)


class ClientTestCase(APITestCase):
    url = '/client/'

    def setUp(self):
        self.username = "jessicapaz"
        self.password = "test"
        self.user = User.objects.create_user(self.username, self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_client(self):
        data = {
          "name": "Jessica",
          "rg": "456446",
          "cpf": "465468865",
          "phone": "45465464",
          "client": {
            "email": "jessica@gmail.com"
            }
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(json.loads(response.content), data)
