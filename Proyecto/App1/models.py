from django.db import models

PROVINCIAS_ARGENTINAS = (
    ('Buenos Aires', 'Buenos Aires'),
    ('C.A.B.A.', 'C.A.B.A.'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucumán'),
)

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    provincia = models.CharField(max_length=100, choices=PROVINCIAS_ARGENTINAS,default="Buenos Aires")
    CUIT = models.IntegerField()
    email = models.EmailField()

class Vendedores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    provincia=models.CharField(max_length=100, choices=PROVINCIAS_ARGENTINAS,default="Buenos Aires")
    CUIT=models.IntegerField()
    email=models.EmailField()
    comision_porc=models.IntegerField()

class Productos(models.Model):
    descripcion=models.CharField(max_length=40)
    unidad=models.CharField(max_length=5)  #kg,m,bolsa,caja,etc
    precio_unit=models.FloatField()
    stock=models.FloatField()
    exento=models.BooleanField()  #Si el producto tiene eximición impositiva o no. 21 vs 10,5.

class RecursosHumanos(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    CUIT=models.IntegerField()
    email=models.EmailField()
    descripcion=models.CharField(max_length=100)
    CV=models.FileField(upload_to="CVs")
