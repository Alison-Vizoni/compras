from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.categoria.models import Categoria
from apps.categoria.serializers import CategoriaSerializers


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
