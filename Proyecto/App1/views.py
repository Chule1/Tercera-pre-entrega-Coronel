from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

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