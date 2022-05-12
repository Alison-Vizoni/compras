
from rest_framework import serializers

from apps.cidade.models import Cidade


class CidadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('__all__')
