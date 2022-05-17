from django.db import models

from apps.estado.models import Estado


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, null=False)
