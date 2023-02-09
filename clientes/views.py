from rest_framework import mixins, generics, permissions
from .models import CLIENTE
from .serializers import ClienteSerializer


class ClienteListAPIView(generics.ListAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]
    queryset = CLIENTE.objects.all()