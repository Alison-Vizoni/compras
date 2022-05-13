from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.estado.models import Estado
from apps.estado.serializers import EstadoSerializers


class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
