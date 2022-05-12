from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField(max_length=10)
