from django.shortcuts import render
from .models import Type, Sneakers,Clients,Orders
from .serializers import SneakerSerializer, TypeSerializer, OrdersSerializer, ClientSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser




class SneakersList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sneakers.objects.all()
    serializer_class = SneakerSerializer
    name = 'sneaker-list'


class SneakerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sneakers.objects.all()
    serializer_class = SneakerSerializer
    name = 'sneakers-detail'
   
class TypeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-list'

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-detail'

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    name = 'clients-detail'

class OrdersList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    name = 'orders-list'

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    name = 'orders-detail'

class RootApi(generics.GenericAPIView):
    name = 'root-api'
    def get(self, request):
        return Response({
            'sneakers': reverse(SneakersList.name, request=request),
            'sneakers-type': reverse(TypeList.name, request=request),
            'client': reverse(ClientList.name, request=request),
            'orders': reverse(OrdersList.name, request=request),
        })


