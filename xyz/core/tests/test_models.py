from django.test import TestCase
from core.models import Person
from core.models import Seller
from core.models import Client
from core.models import ProductService
from core.models import Sale


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            phone="91987523698"
        )

    def test_person_create(self):
        person = Person.objects.first()
        self.assertEqual(person.name, "Jessica Paz")


class SellerTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            phone="91987523698"
        )

        Person.objects.create(
            name="Roger Souza",
            rg="2583356",
            cpf="0327895726",
            phone="91987523698"
        )

        self.person_1 = Person.objects.first()
        Seller.objects.create(
            person=self.person_1,
            salary=5500.67
        )

        self.person_2 = Person.objects.last()
        Client.objects.create(
            person=self.person_2
        )

        ProductService.objects.create(
            type_choice="P",
            name="AAA",
            price=5214.65,
            commission_rate=0.02
        )

        ProductService.objects.create(
            type_choice="S",
            name="AAA",
            price=100,
            commission_rate=0.1
        )

        self.client = Client.objects.first()
        self.seller = Seller.objects.first()

        self.sale_create = Sale(
            seller=self.seller,
            client=self.client,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.product = ProductService.objects.first()
        self.sale_create.product_service.add(self.product)

        self.sale_create = Sale(
            seller=self.seller,
            client=self.client,
            timestamp='2018-11-16T12:00:00Z'
        )
        self.sale_create.save()
        self.service = ProductService.objects.last()
        self.sale_create.product_service.add(self.service)


    def test_saller_create(self):
        saller = Seller.objects.get(pk=1)
        self.assertEqual(saller.person.name, "Jessica Paz")

    def test_seller_commission_per_date(self):
        seller = Seller.objects.first()
        start = "2018-11-13T12:00:00Z"
        end = "2018-11-16T12:00:00Z"
        commission_per_date = seller.commission_per_date(start, end)
        self.assertEqual(commission_per_date, 114.29)

class ClientTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
            phone="91987523698"
        )

        self.person = Person.objects.first()
        Client.objects.create(
            person=self.person
        )

        ProductService.objects.create(
            type_choice="S",
            name="AAA",
            price=100,
            commission_rate=0.1
        )

        self.client = Client.objects.first()
        self.sale_create = Sale(
            client=self.client,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.product = ProductService.objects.first()
        self.sale_create.product_service.add(self.product)

    def test_client_create(self):
        client = Client.objects.get(pk=1)
        self.assertEqual(client.person.rg, "2583356")

    def test_client_products_per_date(self):
        client = Client.objects.first()
        start = "2018-11-13T12:00:00Z"
        end = "2018-11-16T12:00:00Z"
        products_per_date = client.products_per_date(start, end)

        products_name = []
        for products in products_per_date:
            for product in products:
                products_name.append(product.name)

        self.assertEqual(products_name, ["AAA"])


class ProductServiceTestCase(TestCase):
    def setUp(self):
        ProductService.objects.create(
            type_choice="P",
            name="AAA",
            price=5214.65,
            commission_rate=0.02
        )

    def test_product_service_create(self):
        product_service = ProductService.objects.first()
        self.assertEqual(product_service.name, "AAA")
        self.assertNotEqual(product_service.name, 0.5)

    def test_commission(self):
        product_service = ProductService.objects.first()
        commission = product_service.commission
        self.assertEqual(commission, 104.29)


class SaleTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            name="Jessica Paz",
            rg="2583356",
            cpf="03278958256",
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
            commission_rate=0.02
        )

        ProductService.objects.create(
            type_choice="S",
            name="AAA",
            price=100,
            commission_rate=0.1
        )

        self.client = Client.objects.first()
        self.sale_create = Sale(
            client=self.client,
            timestamp='2018-11-13T12:00:00Z'
        )
        self.sale_create.save()
        self.product = ProductService.objects.first()
        self.service = ProductService.objects.last()
        self.sale_create.product_service.add(self.product)
        self.sale_create.product_service.add(self.service)

    def test_sale_create(self):
        sale = Sale.objects.first()
        self.assertEqual(sale.client.person.name, "Jessica Paz")

    def test_total_commission(self):
        sale = Sale.objects.first()
        total_commission = sale.total_commission
        self.assertEqual(total_commission, 114.29)

    def test_top_products_per_date(self):
        sale = Sale.objects.first()
        start = "2018-11-13T12:00:00Z"
        end = "2018-11-16T12:00:00Z"
        products_per_date = sale.top_products_per_date(start, end)

        self.assertEqual(len(products_per_date), 1)
