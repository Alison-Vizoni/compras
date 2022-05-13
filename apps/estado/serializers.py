from rest_framework import serializers

from apps.estado.models import Estado


class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')