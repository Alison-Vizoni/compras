from rest_framework import serializers

from apps.pedido.models import Pedido


class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('__all__')