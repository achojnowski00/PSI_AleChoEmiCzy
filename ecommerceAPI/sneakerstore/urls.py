from django.urls import path
from . import views

urlpatterns = [
    path('sneakers', views.SneakersList.as_view(), name=views.SneakersList.name),
    path('sneakers/<int:pk>', views.SneakerDetail.as_view(), name=views.SneakerDetail.name),
    path('type', views.TypeList.as_view(), name=views.TypeList.name),
    path('type/<int:pk>', views.TypeDetail.as_view(), name=views.TypeDetail.name),
    path('client', views.ClientList.as_view(), name=views.ClientList.name),
    path('client/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('orders', views.OrdersList.as_view(), name=views.OrdersList.name),
    path('orders/<int:pk>', views.OrdersDetail.as_view(), name=views.OrdersDetail.name),
    path('', views.RootApi.as_view(), name=views.RootApi.name),

]