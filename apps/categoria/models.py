from django.db import models

from apps.produto.models import Produto


class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    produto = models.ManyToManyField(Produto)
