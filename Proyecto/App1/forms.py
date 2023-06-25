from django import forms
from forms import PROVINCIAS_ARGENTINAS

class RegistrarCliente(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    provincia=forms.CharField(max_length=100, choices=PROVINCIAS_ARGENTINAS,default="Buenos Aires")
    CUIT=forms.IntegerField()
    email=forms.EmailField()

class RegistrarVendedor(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    provincia=forms.CharField(max_length=100, choices=PROVINCIAS_ARGENTINAS,default="Buenos Aires")
    CUIT=forms.IntegerField()
    email=forms.EmailField()

class RegistrarProducto(forms.Form):
    descripcion=forms.CharField(max_length=40)
    unidad=forms.CharField(max_length=5)  #kg,m,bolsa,caja,etc
    precio_unit=forms.FloatField()
    stock=forms.FloatField()
    exento=forms.BooleanField()  #Si el producto tiene eximición impositiva o no. 21 vs 10,5.

class RegistrarCandidato(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    CUIT=forms.IntegerField()
    email=forms.EmailField()
    descripcion=forms.CharField(max_length=100)
    CV=forms.FileField(upload_to="CVs")