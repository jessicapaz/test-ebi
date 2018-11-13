from django.test import TestCase
from core.models import Address
from core.models import Person
from core.models import Seller


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
        person = Person.objects.get(pk=1)
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
            salary=5500
        )
    
    def test_saller_create(self):
        saller = Seller.objects.get(pk=1)
        self.assertEqual(saller.person.name, "Jessica Paz")