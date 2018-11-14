import json

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from core.models import Seller
from core.models import Person
from core.models import Client
from core.models import ProductService


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


class ProductServiceTesteCase(APITestCase):
    url = '/product-service/'

    def setUp(self):
        self.username = "jessicapaz"
        self.password = "test"
        self.user = User.objects.create_user(self.username, self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_product_service(self):
        data = {
            "type_choice": "S",
            "name": "service",
            "description": "aaa",
            "price": 454.00,
            "commission_rate": 0.02
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.content, data)


class SaleTesteCase(APITestCase):
    url = '/sale/'

    def setUp(self):
        self.username = "jessicapaz"
        self.password = "test"
        self.user = User.objects.create_user(self.username, self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.person_1 = Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278900256",
            phone="91987523698"
        )
        self.person_2 = Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="0327838256",
            phone="91987523698"
        )

        self.person_1 = Person.objects.first()
        self.seller = Seller.objects.create(
            person=self.person_1,
            salary=5500.67
        )

        self.person_2 = Person.objects.last()
        self.client_ = Client.objects.create(
            person=self.person_2
        )

        self.product_1 = ProductService.objects.create(
            type_choice="P",
            name="AAA",
            price=5214.65,
            commission_rate=0.02
        )

        self.product_2 = ProductService.objects.create(
            type_choice="S",
            name="AAA",
            price=100,
            commission_rate=0.1
        )

    def test_create_sale(self):
        product = ProductService.objects.first()
        service = ProductService.objects.last()
        seller = Seller.objects.first()
        client_ = Client.objects.first()
        data = {
            "product_service": [product.id, service.id],
            "seller": seller.id,
            "client": client_.id,
            "timestamp": '2018-08-27T12:00:00Z'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(json.loads(response.content), data)
