from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

from apps.pedido.models import Pedido
from apps.pedido.serializers import PedidoSerializers


class PedidoViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
