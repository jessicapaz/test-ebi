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

    def update(self, instance, validated_data):
        seller_data = validated_data.pop('seller')
        seller = Seller.objects.get(person=instance)

        instance.name = validated_data.get('name', instance.name)
        instance.rg = validated_data.get('rg', instance.rg)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        seller.salary = seller_data.get('salary', seller.salary)
        seller.save()

        return instance



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

    def update(self, instance, validated_data):
        client_data = validated_data.pop('client')
        client = Client.objects.get(person=instance)

        instance.name = validated_data.get('name', instance.name)
        instance.rg = validated_data.get('rg', instance.rg)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        client.email = client_data.get('email', client.email)
        client.save()

        return instance


class ProductServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductService
        fields = ('type_choice', 'name', 'description', 'price', 'commission_rate')


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('product_service', 'seller', 'client', 'timestamp')
