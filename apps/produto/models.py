from django.db import models

from apps.categoria.models import Categoria
from apps.cliente.models import Cliente


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField(max_length=10)
    cliente_proprietario = models.ForeignKey(Cliente, models.DO_NOTHING, null=False)
    categoria = models.ManyToManyField(Categoria)
