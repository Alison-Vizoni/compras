from rest_framework import serializers

from apps.categoria.models import Categoria


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')