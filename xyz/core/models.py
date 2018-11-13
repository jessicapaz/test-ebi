from django.db import models


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
    salary = models.IntegerField()
