
from django.contrib import admin
from django.urls import path
from clientes import views

app_name='CLIENTE'


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cliente/',views.ClienteListAPIView.as_view(),name='cliente-list'),

]
