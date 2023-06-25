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
    if request.method == "POST":
        var_cliente= Clientes(request.POST["nombre"],request.POST["apellido"],request.POST["provincia"],request.POST["CUIT"],request.POST["email"])
        var_cliente.save()
        return render(request,"inicio.html")
    return render(request, "RegistrarCliente.html")

# """if request.method == 'POST':
#        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
#        estudiante.save()
#        return render(request,"AppCoder/inicio.html")
#    return render(request, "AppCoder/setEstudiantes.html")"""