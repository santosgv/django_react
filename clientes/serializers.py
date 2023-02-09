from rest_framework import serializers

from.models import CLIENTE

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLIENTE
        fields = ('id','NOME','LOGRADOURO','NUMERO','BAIRRO','CIDADE','TELEFONE','CPF')
        read_only_fields = ('id',)