from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Person
from .models import Seller
from .models import Client
from .models import ProductService
from .models import Sale
from .serializers import PersonSellerSerializer
from .serializers import PersonClientSerializer
from .serializers import ProductServiceSerializer
from .serializers import SaleSerializer
from rest_framework import status


class SellerViewSet(viewsets.ViewSet):

    queryset = Person.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PersonSellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "name": request.data["name"],
                "rg": request.data["rg"],
                "cpf": request.data["cpf"],
                "phone": request.data["phone"],
                "seller": request.data["seller"]
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(viewsets.ViewSet):

    queryset = Client.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PersonClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "name": request.data["name"],
                "rg": request.data["rg"],
                "cpf": request.data["cpf"],
                "phone": request.data["phone"],
                "client": request.data["client"]
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductServiceView(generics.ListCreateAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


class SaleView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
