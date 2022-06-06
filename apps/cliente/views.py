from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from apps.cliente.models import Cliente
from apps.cliente.serializers import ClienteSerializers


class ClienteViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
