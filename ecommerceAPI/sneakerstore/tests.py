from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import Clients, Sneakers
from rest_framework import status
from django.contrib.auth.models import User


# Create your tests here.
class SneakersTests(APITestCase):
    def create_sneaker_type(self, client):
        url = reverse(views.TypeList.name)
        data = {'id_type': 1,'name_type':'slides'}
        client.post(url, data, format='json')

    def create_sneaker(self,name, price , stock, brand_name, size, color_way, type,owner, client):
        url = reverse(views.SneakersList.name)
        data = {'name': name,
                'price': price,
                'stock': stock,
                'brand_name': brand_name,
                'size': size,
                'color_way': color_way,
                'type': type,
                'owner': owner}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_sneaker(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        self.create_sneaker_type(client)
        new_name = 'Yeezy Slides'
        new_price = 1300
        new_stock= 2
        new_brand_name = 'Adidas'
        new_size = 39
        new_color_way = 'Core'
        new_type = 'slides'
        response = self.create_sneaker(new_name,new_price,new_stock,new_brand_name,new_size, new_color_way,new_type,user.id , client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Sneakers.objects.count() == 1
        assert Sneakers.objects.get().name == new_name
        assert Sneakers.objects.get().brand_name == new_brand_name

    
    class ClientTests(APITestCase):
        def create_client(self,  first_name, last_name, address, email, birth_date, client):
            url = reverse(views.ClientList.name)
            data = { 'first_name':first_name,
                    'last_name': last_name,
                    'address': address,
                    'email':email,
                    'birth_date':birth_date,}
            response = client.post(url, data, format='json')
            return response

        def test_post_and_get_client(self):
            User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
            client = APIClient()
            client.login(username='admin', password='admin123')
            new_first_name = 'Anna'
            new_last_name = 'Kowalska'
            new_address = 'Wspólna 22 44-123 Gdańsk'
            new_email = 'annakowalska@gmail.com'
            new_birthdate = '1999-04-05'
            response = self.create_client(new_first_name,new_last_name,new_address,new_email,new_birthdate, client)
            assert response.status_code == status.HTTP_201_CREATED
            assert Clients.objects.count() == 1
            assert Clients.objects.get().first_name == new_first_name
            assert Clients.objects.get().last_name == new_last_name
            assert Clients.objects.get().email == new_email
        

