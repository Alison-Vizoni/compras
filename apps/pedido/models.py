from django.db import models


class Pedido(models.Model):
    instante = models.DateTimeField()
