from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from apps.categoria.models import Categoria
from apps.categoria.serializers import CategoriaSerializers


class CategoriaViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    http_method_names = ['get']
