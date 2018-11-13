from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    name = models.CharField(
        max_length=50
    )
    rg = models.CharField(
        max_length=14
    )
    cpf = models.CharField(
        max_length=11
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=11
    )


class Address(models.Model):
    streat = models.CharField(
        max_length=50
    )
    number = models.CharField(
        max_length=6
    )
    neighborhood = models.CharField(
        max_length=20
    )
    zip_code = models.CharField(
        max_length=8
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


class Client(models.Model):
    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE
    )


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
    commission = models.FloatField(
        validators=[MaxValueValidator(1.0), MinValueValidator(0.0)]
    )