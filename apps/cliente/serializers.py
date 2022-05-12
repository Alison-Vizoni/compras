from rest_framework import serializers

from apps.cliente.models import Cliente


class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')