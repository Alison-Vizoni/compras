from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.produto.models import Produto
from apps.produto.serializers import ProdutoSerializers


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
