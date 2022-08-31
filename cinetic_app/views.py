from django.shortcuts import render
from cinetic_app.models import *
from cinetic_app.serializers import *
from rest_framework import viewsets, status

class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

class VendeProductos_view(viewsets.ModelViewSet):
    queryset = VendeProductos.objects.all()
    serializer_class = VendeProductos_serializer

class VendeBoletas_view(viewsets.ModelViewSet):
    queryset = VendeBoletas.objects.all()
    serializer_class = VendeBoletas_serializer

class Producto_view(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer

class Combo_view(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = Combo_serializer

class IntegraCombo_view(viewsets.ModelViewSet):
    queryset = IntegraCombo.objects.all()
    serializer_class = IntegraCombo_serializer

class ListaCompras_view(viewsets.ModelViewSet):
    queryset = ListaCompras.objects.all()
    serializer_class = ListaCompras_serializer

class Pelicula_view(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = Pelicula_serializer

class Cinema_view(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = Cinema_serializer

class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = Sala_serializer

class Funcion_view(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = Funcion_serializer

class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = Boleta_serializer


