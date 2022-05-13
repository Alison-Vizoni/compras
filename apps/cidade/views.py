from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.cidade.models import Cidade
from apps.cidade.serializers import CidadeSerializers


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
