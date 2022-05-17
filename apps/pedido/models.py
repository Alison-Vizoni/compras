from django.db import models

from apps.cliente.models import Cliente
from apps.produto.models import Produto


class Pedido(models.Model):
    instante = models.DateTimeField()
    produto = models.ManyToManyField(Produto)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null=False)
