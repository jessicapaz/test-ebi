from django.db import models
from django.apps import apps

from collections import Counter
from operator import add
from functools import reduce


class ProductManager(models.Manager):
    def most_sold(self, start=0, end=0):
        sale_model = apps.get_model('core', 'Sale')
        sales = sale_model.objects.filter(
            timestamp__range=[start, end]
        )

        counters = []
        for sale in sales:
            counters.append(Counter(sale.product_service.all()))
        return list(reduce(add, counters))


    def client_most_sold(self, start=0, end=0, client=""):
        sale_model = apps.get_model('core', 'Sale')
        sales = sale_model.objects.filter(
            client=client,
            timestamp__range=[start, end]
        )
        products = []
        for sale in sales:
            products += sale.product_service.all()
        return list(products)
