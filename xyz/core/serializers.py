from rest_framework import serializers
from .models import Person
from .models import Seller
from .models import Client
from .models import ProductService
from .models import Sale


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('salary',)
        depth = 2


class PersonSellerSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(required=True)

    class Meta:
        model = Person
        fields = ('name', 'rg', 'cpf', 'phone', 'seller')

    def create(self, validated_data):
        seller_data = validated_data.pop('seller')
        person = Person.objects.create(**validated_data)
        Seller.objects.create(person=person, **seller_data)
        return person


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('email',)


class PersonClientSerializer(serializers.ModelSerializer):
    client = ClientSerializer(required=True)

    class Meta:
        model = Person
        fields = ('name', 'rg', 'cpf', 'phone', 'client')

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        person = Person.objects.create(**validated_data)
        Client.objects.create(person=person, **client_data)
        return person

class ProductServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductService
        fields = ('type_choice', 'name', 'description', 'price', 'commission_rate')


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('product_service', 'seller', 'client', 'timestamp')
