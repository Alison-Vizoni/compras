from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from apps.endereco.models import Endereco
from apps.endereco.serializers import EnderecoSerializers


class EnderecoViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
