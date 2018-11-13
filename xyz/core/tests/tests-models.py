from django.test import TestCase
from core.models import Address
from core.models import Person
from core.models import Seller
from core.models import Client
from core.models import ProductService
from core.models import Sale


class PersonTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            streat="Av X",
            number="25",
            neighborhood="40 horas",
            zip_code="67128069"
        )

        self.address = Address.objects.first()
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            address=self.address,
            phone="91987523698"
        )
    
    def test_person_create(self):
        person = Person.objects.first()
        self.assertEqual(person.name, "Jessica Paz")
        


class AddressTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            streat="Av X",
            number="25",
            neighborhood="40 horas",
            zip_code="67128069"
        )
    
    def test_address_create(self):
        address = Address.objects.get(pk=1)
        self.assertEqual(address.streat, "Av X")


class SellerTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            streat="Av X",
            number="25",
            neighborhood="40 horas",
            zip_code="67128069"
        )

        self.address = Address.objects.first()
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            address=self.address,
            phone="91987523698"
        )

        self.person = Person.objects.first()
        Seller.objects.create(
            person=self.person,
            salary=5500.67
        )
    
    def test_saller_create(self):
        saller = Seller.objects.get(pk=1)
        self.assertEqual(saller.person.name, "Jessica Paz")


class ClientTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            streat="Av X",
            number="25",
            neighborhood="40 horas",
            zip_code="67128069"
        )

        self.address = Address.objects.first()
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            address=self.address,
            phone="91987523698"
        )

        self.person = Person.objects.first()
        Client.objects.create(
            person=self.person
        )
    
    def test_client_create(self):
        client = Client.objects.get(pk=1)
        self.assertEqual(client.person.rg, "2583356")


class ProductServiceTestCase(TestCase):
    def setUp(self):
        ProductService.objects.create(
            type_choice="P",
            name="AAA",
            price=5214.65,
            commission=0.2
        )
    
    def test_product_service_create(self):
        product_service = ProductService.objects.first()
        self.assertEqual(product_service.name, "AAA")
        self.assertNotEqual(product_service.name, 0.5)


class SaleTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            streat="Av X",
            number="25",
            neighborhood="40 horas",
            zip_code="67128069"
        )

        self.address = Address.objects.first()
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            address=self.address,
            phone="91987523698"
        )

        self.person = Person.objects.first()
        Client.objects.create(
            person=self.person
        )

        ProductService.objects.create(
            type_choice="P",
            name="AAA",
            price=5214.65,
            commission=0.2
        )

        self.product_service = ProductService.objects.first()
        self.client = Client.objects.first()
        self.sale_create = Sale(
            client=self.client,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.sale_create.product_service.add(self.product_service)

        

    def test_sale_create(self):
        sale = Sale.objects.first()
        self.assertEqual(sale.client.person.name, "Jessica Paz")