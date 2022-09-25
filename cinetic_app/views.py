from cinetic_app.serializers import *
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password, is_active=True)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['caratula'] == '':
            datos.pop('caratula')

        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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

