from django.contrib import admin
from .models import Type, Sneakers, Clients, Orders

# Register your models here.

admin.site.register(Type)
admin.site.register(Sneakers)
admin.site.register(Clients)
admin.site.register(Orders)