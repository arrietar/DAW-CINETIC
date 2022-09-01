from django.shortcuts import render
from cinetic_app.models import *
from cinetic_app.serializers import *
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

# Modulo de Productos y Combos

class Producto_view(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer

class Combo_view(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = Combo_serializer

class IntegraCombo_view(viewsets.ModelViewSet):
    queryset = IntegraCombo.objects.all()
    serializer_class = IntegraCombo_serializer

class VentaProducto_view(viewsets.ModelViewSet):
    queryset = VentaProducto.objects.all()
    serializer_class = VentaProducto_serializer

class ListaVentaProducto_view(viewsets.ModelViewSet):
    queryset = ListaVentaProducto.objects.all()
    serializer_class = ListaVentaProducto_serializer

# Modulo de Funciones

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

class VendeBoletas_view(viewsets.ModelViewSet):
    queryset = VentaBoleta.objects.all()
    serializer_class = VentaBoleta_serializer

class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = Boleta_serializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if(token):
            token.delete()
            token, created = Token.objects.get_or_create(user=user)

        user.token = token.key
        user.save()
        usuario = Empleado_serializer(user)
        return Response(usuario.data)
