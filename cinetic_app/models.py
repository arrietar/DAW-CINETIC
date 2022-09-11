from django.db import models
from django.contrib.auth.models import AbstractUser


#class Empleado(models.Model):
class Empleado(AbstractUser):
    identificacion = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now_add=True, null=False)
    token = models.CharField(max_length=255, default='', null=True, blank=True)
    def __str__(self):
        return self.identificacion

# Modulo de Productos y Combos
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, unique=True)
    nombre_producto = models.CharField(max_length=50)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2)
    ciudad = models.CharField(max_length=20)
    inventario = models.IntegerField()
    def __str__(self):
       return self.nombre_producto

class Combo(models.Model):
    codigo_combo = models.CharField(max_length=20, unique=True)
    nombre_combo = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.nombre_combo


class IntegraCombo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    cantidad_producto = models.IntegerField()

class VentaProducto(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField(auto_now_add=True, null=False)

class ListaVentaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.PROTECT, null=True, blank=True)
    venta_producto = models.ForeignKey(VentaProducto, on_delete=models.PROTECT, null=False)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

# Modulo de Funciones
class Pelicula(models.Model):
    codigo_pelicula = models.CharField(max_length=20, unique=True)
    nombre_pelicula = models.CharField(max_length=50)
    GENERO = [
        ('ACC', 'Accion'),
        ('AVR', 'Aventuras'),
        ('CFN', 'Ciencia ficcion'),
        ('COM', 'Comedia'),
        ('RMT', 'Romantica'),
        ('DRM', 'Drama'),
        ('TRR', 'Terror'),
    ]
    genero = models.CharField(max_length=3, choices=GENERO, default='ACC')

    CLASIFICACION = [
        ('A', 'Infantil'),
        ('AA', 'Todo publico'),
        ('B', 'Mayores de 12'),
        ('B15', 'Mayores de 15'),
        ('C', 'Mayores de 18'),
        ('D', 'Con contenido explicito'),
    ]
    clasificacion = models.CharField(max_length=3, choices=CLASIFICACION, default='A')
    fecha_filmacion = models.DateField(auto_now=False, null=True)
    sinopsis = models.CharField(max_length=255)
    duracion = models.IntegerField()
    caratula = models.ImageField(upload_to='peliculas/')

    def __str__(self):
        return self.nombre_pelicula

class Cinema(models.Model):
    codigo_cinema = models.CharField(max_length=20, unique=True)
    nombre_cinema = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo_cinema


class Sala(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    codigo_sala = models.CharField(max_length=20, unique=True)
    nombre_sala = models.CharField(max_length=50)
    TIPO_SALA = [
        ('2D', '2D'),
        ('3D', '3D'),
    ]
    tipo_sala = models.CharField(max_length=2, choices=TIPO_SALA, default='2D')
    def __str__(self):
        return self.codigo_sala

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    codigo_funcion = models.CharField(max_length=20, unique=True)
    horario = models.TimeField(auto_now=False)
    fecha = models.DateField(auto_now=False, null=True)
    def __str__(self):
        return self.codigo_funcion

class VentaBoleta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField(auto_now_add=True, null=False)
    total = models.IntegerField() # ¿Como se calcula?, CarlosA: no lo entiendo

class Boleta(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    venta_boleta = models.ForeignKey(VentaBoleta, on_delete=models.PROTECT)
    numero_silla = models.CharField(max_length=3)
    valor_boleta = models.DecimalField(max_digits=10, decimal_places=2)



