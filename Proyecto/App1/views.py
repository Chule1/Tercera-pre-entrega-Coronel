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
    if request.method=='POST':
        miFormulario=form_RegistrarVendedor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            vendedor=Vendedores(nombre=data["nombre"],apellido=data["apellido"],provincia=data["provincia"],CUIT=data["CUIT"],email=data["email"],comision_porc=data["comision_porc"])
            vendedor.save()
            return render(request,"inicio.html")    
    else: 
        miFormulario=form_RegistrarVendedor()
    return render(request, "RegistrarVendedor.html", {"miFormulario":miFormulario})

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
    if request.method=='POST':
        miFormulario=form_RegistrarProducto(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            producto=Productos(descripcion=data["descripcion"],unidad=data["unidad"],precio_unit=data["precio_unit"],stock=data["stock"])
            producto.save()
            return render(request,"inicio.html")    
    else: 
        miFormulario=form_RegistrarProducto()
    return render(request, "RegistrarProducto.html", {"miFormulario":miFormulario})

def BuscarProducto(request):
    return render(request, "BuscarProducto.html")

def aux_BuscarProducto(request):
    if request.GET["descripcion"]:
        descripcion=request.GET["descripcion"]
        productos = Productos.objects.filter(descripcion = descripcion)
        return render(request, "BuscarProducto.html", {"productos":productos})
    else: 
        respuesta = "No se enviaron datos"   
    return HttpResponse(respuesta)


def RegistrarCandidato(request):
    if request.method=='POST':
        miFormulario=form_RegistrarCandidato(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            candidato=RecursosHumanos(nombre=data["nombre"],apellido=data["apellido"],CUIT=data["CUIT"],email=data["email"],provincia=data["provincia"],CV=data["CV"])
            candidato.save()
            return render(request,"inicio.html")    
    else: 
        miFormulario=form_RegistrarCandidato()
    return render(request, "RegistrarCandidato.html", {"miFormulario":miFormulario})
