from django.db import models

from apps.cidade.models import Cidade


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=150, null=True, default="", blank=True)
    bairro = models.CharField(max_length=150, null=True)
    cep = models.CharField(max_length=9)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, null=False)
