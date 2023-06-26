from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from App1.forms import *
from App1.models import *
from django import forms

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def clientes(request):
    return render(request, "Clientes.html")

def vendedores(request):
    return render(request, "Vendedores.html")

def productos(request):
    return render(request, "Productos.html")

def recursosHumanos(request):
    return render(request, "RecursosHumanos.html")

def Empty(request):
    return render(request, "Empty.html")

def RegistrarCliente(request):
    if request.method=='POST':
        miFormulario=form_RegistrarCliente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            cliente=Clientes(nombre=data["nombre"],apellido=data["apellido"],provincia=data["provincia"],CUIT=data["CUIT"],email=data["email"])
            cliente.save()
            return render(request,"inicio.html")    
    else: 
        miFormulario=form_RegistrarCliente()
    return render(request, "RegistrarCliente.html", {"miFormulario":miFormulario})

def RegistrarVendedor(request):
    return render(request, "RegistrarVendedor.html")

def BuscarVendedor(request):
    return render(request, "BuscarVendedor.html")

def aux_BuscarVendedor(request):
    if request.GET["provincia"]:
        provincia=request.GET["provincia"]
        vendedores = Vendedores.objects.filter(provincia = provincia)
        return render(request, "BuscarVendedor.html", {"vendedores":vendedores})
    else: 
        respuesta = "No se enviaron datos"   
    return HttpResponse(respuesta)

def RegistrarProducto(request):
    return render(request, "RegistrarProducto.html")

def BuscarProducto(request):
    return render(request, "BuscarProducto.html")
