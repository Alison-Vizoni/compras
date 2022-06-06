from django.db import models
from django.utils.translation import gettext_lazy

from apps.endereco.models import Endereco


class TipoCliente(models.TextChoices):
    PESSOA_FISICA = "PESSOA_FISICA", gettext_lazy('Pessoa física')
    PESSOA_JURIDICA = "PESSOA_JURIDICA", gettext_lazy('Pessoa jurídica')


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    cpf_ou_cnpj = models.CharField(max_length=20)
    tipo = models.CharField(
        max_length=15,
        choices=TipoCliente.choices,
    )
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, null=False)
