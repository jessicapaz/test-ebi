import json

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from core.models import Seller
from core.models import Person
from core.models import Client
from core.models import ProductService
from core.models import Sale


class SellerTestCase(APITestCase):
    url = '/seller/'

    def setUp(self):
        self.username = "jessicapaz"
        self.password = "test"
        self.user = User.objects.create_user(self.username, self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.person = Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03241258789",
            phone="91987857598"
        )
        self.seller = Seller.objects.create(
            person=self.person,
            salary=5500.67
        )

    def test_create_seller(self):
        data = {
          "name": "Jessica",
          "rg": "456446",
          "cpf": "03247898565",
          "phone": "9981875978",
          "seller": {
            "salary": 6554.6
            }
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(json.loads(response.content), data)

    def test_update_seller(self):
        person_id = self.person.id

        data = {
          "name": "Ana",
          "rg": "456446",
          "cpf": "03247898565",
          "phone": "9981875978",
          "seller": {
            "salary": 6554.6
            }
        }
        response = self.client.put(f'{self.url}{person_id}/', data=data, format='json')
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

        self.person = Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03241258789",
            phone="91987857598"
        )
        self.client_ = Client.objects.create(
            person=self.person,
            email="test@gmail.com"
        )

    def test_create_client(self):
        data = {
          "name": "Jessica",
          "rg": "456446",
          "cpf": "03278987458",
          "phone": "91987857898",
          "client": {
            "email": "test@gmail.com"
            }
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(json.loads(response.content), data)

    def test_update_client(self):
        person_id = self.person.id

        data = {
          "name": "Ana",
          "rg": "456446",
          "cpf": "03247898565",
          "phone": "9981875978",
          "client": {
            "email": "test@gmail.com"
            }
        }
        response = self.client.put(f'{self.url}{person_id}/', data=data, format='json')
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
        self.product = ProductService.objects.create(
            type_choice="P",
            name="AAA",
            description="a",
            price=5214.65,
            commission_rate=0.02
        )

    def test_create_product_service(self):
        data = {
            "type_choice": "S",
            "name": "service",
            "description": "aaa",
            "price": 454.00,
            "commission_rate": 0.02
        }
        response = self.client.post(self.url, data=data, format='json')
        data["price"] = "454.00"
        self.assertEqual(json.loads(response.content), data)

    def test_update_product_service(self):
        product_id = self.product.id
        data = {
            "type_choice": "S",
            "name": "se",
            "description": "desc",
            "price": 454.00,
            "commission_rate": 0.02
        }
        response = self.client.put(f'{self.url}{product_id}/', data=data)
        data["price"] = "454.00"
        self.assertEqual(json.loads(response.content), data)

    def test_delete_product_service(self):
        product_id = self.product.id
        response = self.client.delete(f'{self.url}{product_id}/')
        self.assertEqual(response.status_code, 204)


class SaleTestCase(APITestCase):
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
        self.sale = Sale.objects.create(
            seller=self.seller,
            client=self.client_,
            timestamp='2018-11-13T12:00:00Z'
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

    def test_update_sale(self):
        product = ProductService.objects.first()
        service = ProductService.objects.last()
        seller = Seller.objects.first()
        client_ = Client.objects.first()
        sale_id = self.sale.id
        data = {
            "product_service": [product.id, service.id],
            "seller": seller.id,
            "client": client_.id,
            "timestamp": '2017-08-27T10:00:00Z'
        }
        response = self.client.put(f'{self.url}{sale_id}/', data=data)
        self.assertEqual(json.loads(response.content), data)

    def test_delete_sale(self):
        sale_id = self.sale.id
        response = self.client.delete(f'{self.url}{sale_id}/')
        self.assertEqual(response.status_code, 204)


class SellerCommissionTestCase(APITestCase):
    url = '/seller-commission/'

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

        self.sale_create = Sale(
            client=self.client_,
            seller=self.seller,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.product = ProductService.objects.first()
        self.service = ProductService.objects.last()
        self.sale_create.product_service.add(self.product)
        self.sale_create.product_service.add(self.service)

    def test_get_commission(self):
        data = {
            "total-commission" : 114.29
        }
        response = self.client.get(
            f'{self.url}?start=2018-08-27&end=2018-12-13&cpf=03278900256'
        )
        self.assertEqual(json.loads(response.content), data)


class MostSoldTestCase(APITestCase):
    url = '/most-sold/'

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

        self.seller = Seller.objects.create(
            person=self.person_1,
            salary=5500.67
        )

        self.client_ = Client.objects.create(
            person=self.person_2
        )

        self.service = ProductService.objects.create(
            type_choice="S",
            name="p 2",
            price=100,
            commission_rate=0.1
        )

        self.sale_create = Sale(
            client=self.client_,
            seller=self.seller,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.sale_create.product_service.add(self.service)


    def test_most_sold_per_date(self):
        data = [
            {
                "type_choice": "S",
                "name": "p 2",
                "price": "100.00",
                "commission_rate": 0.1,
                'description': '',
            }]
        response = self.client.get(
        f'{self.url}?start=2018-08-27 12:00&end=2018-12-13 12:00')
        self.assertEqual(json.loads(response.content), data)


class ClientProductsTestCase(APITestCase):
    url = '/client-most-sold/'

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

        self.seller = Seller.objects.create(
            person=self.person_1,
            salary=5500.67
        )

        self.client_ = Client.objects.create(
            person=self.person_2
        )

        self.service = ProductService.objects.create(
            type_choice="S",
            name="p 2",
            price=100,
            commission_rate=0.1
        )

        self.sale_create = Sale(
            client=self.client_,
            seller=self.seller,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.sale_create.product_service.add(self.service)


    def test_client_products_per_date(self):
        data = [
            {
                "type_choice": "S",
                "name": "p 2",
                "price": "100.00",
                "commission_rate": 0.1,
                'description': '',
            }]
        response = self.client.get(
            f'{self.url}?start=2018-08-27 12:00&end=2018-12-13 12:00&cpf=0327838256'
        )
        self.assertEqual(json.loads(response.content), data)
