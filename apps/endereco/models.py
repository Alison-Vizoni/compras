from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=150, null=True)
    bairro = models.CharField(max_length=150, null=True)
    cep = models.CharField(max_length=9, null=False)

