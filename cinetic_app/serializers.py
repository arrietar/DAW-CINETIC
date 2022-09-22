from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from cinetic_app.models import *


class Empleado_serializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'

# Modulo de Productos y Combos
class Producto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class Combo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'

class IntegraCombo_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    id_producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_serializer(read_only=True)
    id_combo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    class Meta:
        model = IntegraCombo
        fields = '__all__'

class VentaProducto_serializer(serializers.ModelSerializer):
    empleado = Empleado_serializer(read_only=True)
    id_empleado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = VentaProducto
        fields = '__all__'

class ListaVentaProducto_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    id_producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto', required=False, allow_null=True)
    combo = Combo_serializer(read_only=True)
    id_combo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo', required=False, allow_null=True)
    venta_producto = VentaProducto_serializer(read_only=True)
    id_venta_producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VentaProducto.objects.all(), source='venta_producto')
    class Meta:
        model = ListaVentaProducto
        fields = '__all__'


# Modulo de Funciones

class Pelicula_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class Cinema_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class Sala_serializer(serializers.ModelSerializer):
    cinema = Cinema_serializer(read_only=True)
    codigo_cinema = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cinema.objects.all(), source='cinema')
    class Meta:
        model = Sala
        fields = '__all__'

class Funcion_serializer(serializers.ModelSerializer):
    pelicula = Pelicula_serializer(read_only=True)
    id_pelicula = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(), source='pelicula')
    sala = Sala_serializer(read_only=True)
    id_sala = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    class Meta:
        model = Funcion
        fields = '__all__'

class VentaBoleta_serializer(serializers.ModelSerializer):
    empleado = Empleado_serializer(read_only=True)
    id_empleado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = VentaBoleta
        fields = '__all__'

class Boleta_serializer(serializers.ModelSerializer):
    funcion = Funcion_serializer(read_only=True)
    id_funcion = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Funcion.objects.all(), source='funcion')
    venta_boleta = VentaBoleta_serializer(read_only=True)
    id_venta_boleta = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VentaBoleta.objects.all(), source='venta_boleta')
    class Meta:
        model = Boleta
        fields = '__all__'

