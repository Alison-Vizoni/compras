from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.cliente.models import Cliente
from apps.cliente.serializers import ClienteSerializers


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers
    http_method_names = ['get', 'post', 'put', 'delete']