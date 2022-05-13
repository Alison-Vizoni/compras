from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.pedido.models import Pedido
from apps.pedido.serializers import PedidoSerializers


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
