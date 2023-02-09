from django.db import models


class CLIENTE(models.Model):
    NOME = models.CharField(max_length=250)
    LOGRADOURO = models.CharField(max_length=250)
    NUMERO = models.CharField(max_length=10)
    BAIRRO = models.CharField(max_length=200)
    CIDADE = models.CharField(max_length=200)
    TELEFONE = models.CharField(max_length=30, blank=True, null=True)
    CPF = models.CharField(max_length=14)

    def __str__(self) -> str:
        return str(self.NOME)