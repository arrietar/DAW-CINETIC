from django.db import models
from django.contrib.auth.models import AbstractUser

class Empleado(models.Model):
    id_empleado = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    contrasenia = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)

class VendeProductos(models.Model):
    codigo_vende_productos = models.CharField(max_length=20, unique=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateField(auto_now=False, null=True)

class VendeBoletas(models.Model):
    codigo_vende_boletas = models.CharField(max_length=20, unique=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateField(auto_now=False, null=True)
    sillas_vendidas = models.IntegerField() # hace falta una ForeignKey para calcular las sillas_vendidas
    total = models.IntegerField() # ¿Como se calcula?

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, unique=True)
    nombre_producto = models.CharField(max_length=20)
    valor_compra = models.IntegerField()
    valor_venta = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    inventario = models.IntegerField()

class Combo(models.Model):
    codigo_combo = models.CharField(max_length=20, unique=True)
    nombre_combo = models.CharField(max_length=20)
    descuento = models.IntegerField()

class IntegraCombo(models.Model):
    codigo_integra_combo = models.CharField(max_length=20, unique=True)
    codigo_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    codigo_combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    cantidad_producto = models.IntegerField()

class ListaCompras(models.Model):
    codigo_lista_compras = models.CharField(max_length=20, unique=True)
    codigo_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    codigo_combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    codigo_vende_productos = models.ForeignKey(VendeProductos, on_delete=models.PROTECT)
    cantidad_productos = models.IntegerField()
    cantidad_combos = models.IntegerField()
    subtotal = models.IntegerField()

class Pelicula(models.Model):
    codigo_pelicula = models.CharField(max_length=20, unique=True)
    nombre_pelicula = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    clasificacion = models.CharField(max_length=20)
    nombre_director = models.CharField(max_length=50)
    fecha_filmacion = models.DateField(auto_now=False, null=True)
    sinopsis = models.CharField(max_length=100)
    duracion = models.IntegerField()

class Cinema(models.Model):
    codigo_cinema = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Sala(models.Model):
    codigo_sala = models.CharField(max_length=20, unique=True)
    codigo_cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    nombre_sala = models.CharField(max_length=20)
    tipo_sala = models.CharField(max_length=20)
    capacidad = models.IntegerField()

class Funcion(models.Model):
    codigo_funcion = models.CharField(max_length=20, unique=True)
    codigo_pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    codigo_sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    horario = models.CharField(max_length=20)
    fecha = models.DateField(auto_now=False, null=True)

class Boleta(models.Model):
    codigo_boleta = models.CharField(max_length=20, unique=True)
    codigo_funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    codigo_vende_boletas = models.ForeignKey(VendeBoletas, on_delete=models.PROTECT)
    numero_silla = models.CharField(max_length=20)
    valor_boleta = models.IntegerField()

