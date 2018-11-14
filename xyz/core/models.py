from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from collections import Counter
from operator import add
from functools import reduce


class Person(models.Model):
    name = models.CharField(
        max_length=50
    )
    rg = models.CharField(
        max_length=14
    )
    cpf = models.CharField(
        unique=True,
        max_length=11
    )
    phone = models.CharField(
        max_length=11
    )


class Seller(models.Model):
    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE
    )
    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def commission_per_date(self, start, end):
        sales = Sale.objects.filter(
            seller=self,
            timestamp__range=[start, end]
        )
        total = []
        for sale in sales:
            total.append(sale.total_commission)
        return sum(total)


class Client(models.Model):
    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE
    )
    email = models.EmailField()

    def products_per_date(self, start, end):
        sales = Sale.objects.filter(
            client=self,
            timestamp__range=[start, end]
        )
        products = []
        for sale in sales:
            products.append(sale.product_service.all())
        return products


class ProductService(models.Model):
    TYPE_CHOICES = (
        ("P", "Product"),
        ("S", "Service")
    )
    type_choice = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES
    )
    name = models.CharField(
        max_length=30
    )
    description = models.TextField(
        blank=True
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    commission_rate = models.FloatField(
        validators=[MaxValueValidator(0.1), MinValueValidator(0.0)]
    )

    @property
    def commission(self):
        commission = self.commission_rate * float(self.price)
        return round(commission, 2)


class Sale(models.Model):
    product_service = models.ManyToManyField(
        "ProductService"
    )
    seller = models.ForeignKey(
        "Seller",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    client = models.ForeignKey(
        "Client",
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(
        default=timezone.now()
    )

    @property
    def total_commission(self):
        commissions = []
        for product in self.product_service.all():
            commission = product.commission
            commissions.append(commission)
        total = sum(commissions)
        return total

    def top_products_per_date(self, start, end):
        sales = Sale.objects.filter(
            timestamp__range=[start, end]
        )

        counters = []
        product_name = []
        for sale in sales:
            for product in sale.product_service.all():
                product_name.append(product.name)
        counters.append(Counter(product_name))
        return reduce(add, counters)
