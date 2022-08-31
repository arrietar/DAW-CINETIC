from rest_framework import serializers
from cinetic_app.models import *

class Empleado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class VendeProductos_serializer(serializers.ModelSerializer):
    empleado = Empleado_serializer(read_only=True)
    id_empleado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = VendeProductos
        fields = '__all__'

class VendeBoletas_serializer(serializers.ModelSerializer):
    empleado = Empleado_serializer(read_only=True)
    id_empleado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = VendeBoletas
        fields = '__all__'

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
    codigo_producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_serializer(read_only=True)
    codigo_combo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    class Meta:
        model = IntegraCombo
        fields = '__all__'

class ListaCompras_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    codigo_producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_serializer(read_only=True)
    codigo_combo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    vendeProductos = VendeProductos_serializer(read_only=True)
    codigo_vende_productos = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VendeProductos.objects.all(), source='vendeProductos')
    class Meta:
        model = ListaCompras
        fields = '__all__'

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
    sala = Sala_serializer(read_only=True)
    codigo_sala = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    pelicula = Pelicula_serializer(read_only=True)
    codigo_pelicula = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(), source='pelicula')
    class Meta:
        model = Funcion
        fields = '__all__'

class Boleta_serializer(serializers.ModelSerializer):
    funcion = Funcion_serializer(read_only=True)
    codigo_funcion = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Funcion.objects.all(), source='funcion')
    vendeBoletas = VendeBoletas_serializer(read_only=True)
    codigo_vende_boletas = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VendeBoletas.objects.all(), source='vendeBoletas')
    class Meta:
        model = Boleta
        fields = '__all__'
