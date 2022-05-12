from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
