from django.db import models
from django.contrib.auth.models import AbstractUser

#class Empleado(AbstractUser):
class Empleado(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    token = models.CharField(max_length=255, default='', null=True, blank=True)

# Modulo de Productos y Combos
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, unique=True)
    nombre_producto = models.CharField(max_length=50)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2)
    ciudad = models.CharField(max_length=20)
    inventario = models.IntegerField()

class Combo(models.Model):
    codigo_combo = models.CharField(max_length=20, unique=True)
    nombre_combo = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5,decimal_places=2)

class IntegraCombo(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    id_combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    cantidad_producto = models.IntegerField()

class VentaProducto(models.Model):
    id_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateField(auto_now=False, null=True)

class ListaVentaProducto(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True)
    id_combo = models.ForeignKey(Combo, on_delete=models.PROTECT, null=True)
    id_venta_producto = models.ForeignKey(VentaProducto, on_delete=models.PROTECT, null=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

# Modulo de Funciones
class Pelicula(models.Model):
    codigo_pelicula = models.CharField(max_length=20, unique=True)
    nombre_pelicula = models.CharField(max_length=50)
    genero = models.CharField(max_length=20) # pendiente actualizar con enum
    clasificacion = models.CharField(max_length=20) # pendiente actualizar con enum
    nombre_director = models.CharField(max_length=50)
    fecha_filmacion = models.DateField(auto_now=False, null=True)
    sinopsis = models.CharField(max_length=255)
    duracion = models.IntegerField()
    caratula = models.FileField(upload_to='cinetic_app/caratula_peliculas/')

class Cinema(models.Model):
    codigo_cinema = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

class Sala(models.Model):
    id_cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    codigo_sala = models.CharField(max_length=20, unique=True)
    nombre_sala = models.CharField(max_length=50)
    tipo_sala = models.CharField(max_length=20) # pendiente definir con un enum
    capacidad = models.IntegerField()

class Funcion(models.Model):
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    id_sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    codigo_funcion = models.CharField(max_length=20, unique=True)
    horario = models.TimeField(auto_now=False, null=True)
    fecha = models.DateField(auto_now=False, null=True)

class VentaBoleta(models.Model):
    id_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField(auto_now=False, null=True)
    total = models.IntegerField() # ¿Como se calcula?, CarlosA: no lo entiendo

class Boleta(models.Model):
    id_funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    id_vende_boletas = models.ForeignKey(VentaBoleta, on_delete=models.PROTECT)
    numero_silla = models.CharField(max_length=3)
    valor_boleta = models.DecimalField(max_digits=10, decimal_places=2)



