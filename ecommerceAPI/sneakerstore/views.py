from django.shortcuts import render
from .models import Type, Sneakers,Clients,Orders
from .serializers import SneakerSerializer, TypeSerializer, OrdersSerializer, ClientSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters import DateTimeFilter, NumberFilter, FilterSet
from django.contrib.auth.models import User

class SneakerFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Sneakers
        fields = ['min_price', 'max_price', 'name', 'brand_name', 'size']
    

class SneakersList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Sneakers.objects.all()
    serializer_class = SneakerSerializer
    name = 'sneaker-list'
    filter_class = SneakerFilter
    search_fields = ['name', 'brand_name', 'size']
    ordering_fields = ['name', 'brand_name', 'size']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SneakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakerSerializer
    name = 'sneakers-detail'
    
   
class TypeList(generics.ListCreateAPIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-list'
    filter_fields = ['name_type', 'id_type']
    search_fields = ['name_type']
    ordering_fields = ['name_type', 'id_type']

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-detail'


class ClientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='birth_date', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='birth_date', lookup_expr='lte')

    class Meta:
        model = Clients
        fields = ['from_birthdate', 'to_birthdate', 'email']

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filter_class = ClientFilter

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    name = 'clients-detail'

class OrdersFilter(FilterSet):
    fromDate = DateTimeFilter(
        field_name='purchase_date', lookup_expr='gte')
    toDate = DateTimeFilter(
        field_name='purchase_date', lookup_expr='lte')

    class Meta:
        model = Orders
        fields = ['fromDate', 'toDate', 'id_order',
                  'purchase_date', 'sneakers', 'client']

class OrdersList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    name = 'orders-list'
    filter_class = OrdersFilter
    search_fields = ['id_order', 'purchase_date', 'sneakers', 'client']
    ordering_fields = ['id_order', 'purchase_date', 'sneakers', 'client']

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
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


