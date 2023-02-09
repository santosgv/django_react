
from django.contrib import admin
from django.urls import path
from clientes import views

app_name='CLIENTE'

urlpatterns = [
    path('cliente/',views.ClienteListAPIView.as_view(),
         name='cliente-list'),

]
