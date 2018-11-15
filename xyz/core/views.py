from rest_framework import viewsets
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

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



class SellerViewSet(viewsets.ViewSet):
    queryset = Person.objects.all()

    def get_seller_data(self, request):
        data = {
            "name": request.data["name"],
            "rg": request.data["rg"],
            "cpf": request.data["cpf"],
            "phone": request.data["phone"],
            "seller": request.data["seller"]
        }
        return data

    def create(self, request, *args, **kwargs):
        serializer = PersonSellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = self.get_seller_data(request)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = Person.objects.get(pk=pk)
        serializer = PersonSellerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = self.get_seller_data(request)
            return Response(data)



class SellerCommissionView(views.APIView):

    def get(self, request, *args, **kwargs):
        cpf = request.GET.get("cpf")
        start = request.GET.get("start")
        end = request.GET.get("end")
        person = get_object_or_404(Person, cpf=cpf)
        seller = get_object_or_404(Seller, person=person)
        try:
            commission = seller.commission_per_date(start, end)
        except ValidationError:
            raise

        data = {
            "total-commission": commission
        }
        return Response(data, status.HTTP_200_OK)

class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()

    def get_client_data(self, request):
        data = {
            "name": request.data["name"],
            "rg": request.data["rg"],
            "cpf": request.data["cpf"],
            "phone": request.data["phone"],
            "client": request.data["client"]
        }
        return data

    def create(self, request, *args, **kwargs):
        serializer = PersonClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = self.get_client_data(request)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = Person.objects.get(pk=pk)
        serializer = PersonClientSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = self.get_client_data(request)
            return Response(data)

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


class ProductServiceListView(generics.ListCreateAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


class ProductServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


class SaleListView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class MostSelledView(views.APIView):
    def get(self, request, *args, **kwargs):
        start = request.GET.get("start")
        end = request.GET.get("end")
        try:
            top_products = ProductService.objects.most_selled(start, end)
        except TypeError:
            error_message = "no product/service sold on this date range."
            raise NotFound(detail=error_message)

        data = ProductServiceSerializer(top_products, many=True).data
        return Response(data, status.HTTP_200_OK)
