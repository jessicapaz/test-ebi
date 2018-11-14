from rest_framework import serializers
from .models import Person
from .models import Seller
from .models import Client


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
