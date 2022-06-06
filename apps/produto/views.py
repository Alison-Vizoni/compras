from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from apps.produto.models import Produto
from apps.produto.serializers import ProdutoSerializers


class ProdutoViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
