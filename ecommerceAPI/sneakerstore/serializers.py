from django.db.models import fields
from rest_framework import serializers
from .models import Type, Sneakers, Clients, Orders

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    sneakers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sneakers-detail')

    class Meta:
        model = Type
        fields = ['url', 'id_type', 'name_type', 'sneakers']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='orders-detail')
    class Meta:
        model = Clients
        fields = ['url', 'id_client', 'first_name', 'last_name', 'address','email', 'birth_date', 'orders']



class SneakerSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='name_type')

    class Meta:
        model = Sneakers
        fields = ['url', 'id_sneakers', 'name', 'price', 'stock', 'brand_name', 'size', 'color_way', 'type']
    
    def validate_price(self, value):
        if value<=0:
            raise serializers.ValidationError("Don't make price lower or equal to zero", )
        return value
    
    def validate_stock(self, value):
        if value<0:
            raise serializers.ValidationError("Don't make quantity lower or equal to zero", )
        return value
    def validate_size(self, value):
        if value<=0 or value>60:
            raise serializers.ValidationError("Make size in range 1-60", )
        return value
     


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=Clients.objects.all(), slug_field='email')
    sneakers =  serializers.SlugRelatedField(queryset=Sneakers.objects.all(), slug_field='name')
    purchase_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Orders
        fields = ['url', 'id_order', 'price','quantity','purchase_date','payment_method','client','sneakers']

    def validate_price(self, value):
        if value<0:
            raise serializers.ValidationError("Don't make price lower to zero", )
        return value
    def validate_quantity(self, value):
        if value<=0:
            raise serializers.ValidationError("Don't make quantity lower to zero", )
        return value






    