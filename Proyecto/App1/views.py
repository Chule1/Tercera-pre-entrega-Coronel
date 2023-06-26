from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from App1.forms import *
from App1.models import *

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def Clientes(request):
    return render(request, "Clientes.html")

def Vendedores(request):
    return render(request, "Vendedores.html")

def Productos(request):
    return render(request, "Productos.html")

def RecursosHumanos(request):
    return render(request, "RecursosHumanos.html")

def Empty(request):
    return render(request, "Empty.html")

def RegistrarCliente(request):
    if request.method == 'POST':
        miFormulario= form_RegistrarCliente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            cliente = Clientes(nombre=data["nombre"],apellido=data["apellido"],provincia=data["provincia"],CUIT=data["CUIT"],email=data["email"])
            cliente.save()
            return render(request,"inicio.html")    
    else: 
        miFormulario = form_RegistrarCliente()
    return render(request, "RegistrarCliente.html", {"miFormulario":miFormulario})