from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    CUIT=models.IntegerField()
    email=models.EmailField()

class Vendedores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
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
