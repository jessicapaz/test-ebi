from rest_framework import viewsets
from rest_framework import generics
from rest_framework import views
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


class SellerCommissionView(views.APIView):

    def get(self, request, *args, **kwargs):
        cpf = request.GET.get("cpf")
        start = request.GET.get("start")
        end = request.GET.get("end")
        person = get_object_or_404(Person, cpf=cpf)
        client = get_object_or_404(Client, person=person)
        commission = seller.commission_per_date(start, end)
        data = {
            "total-commission": commission
        }
        return Response(data, status.HTTP_200_OK)

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

class ClientProductsView(views.APIView):

    def get(self, request, *args, **kwargs):
        cpf = request.GET.get("cpf")
        start = request.GET.get("start")
        end = request.GET.get("end")
        person = get_object_or_404(Person, cpf=cpf)
        client = get_object_or_404(Client, person=person)
        client_most_selled = ProductService.objects.client_most_selled(start, end, client)
        data = ProductServiceSerializer(client_most_selled, many=True).data
        return Response(data, status.HTTP_200_OK)

class ProductServiceView(generics.ListCreateAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


class SaleView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class TopProductsView(views.APIView):
    def get(self, request, *args, **kwargs):
        start = request.GET.get("start")
        end = request.GET.get("end")
        top_products = ProductService.objects.most_selled(start, end)
        data = ProductServiceSerializer(top_products, many=True).data

        return Response(data, status.HTTP_200_OK)
