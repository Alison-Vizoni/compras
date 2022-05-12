from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.endereco.models import Endereco
from apps.endereco.serializers import EnderecoSerializers


class EnderecoViewSet(ModelViewSet):
    query = Endereco.objects.all()
    serializer_class = EnderecoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
