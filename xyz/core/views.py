from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Person
from .models import Seller
from .serializers import PersonSellerSerializer
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
