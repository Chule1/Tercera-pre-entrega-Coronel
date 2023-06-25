from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "App1/inicio.html")

def Clientes(request):
    return render(request, "App1/Clientes.html")

def Vendedores(request):
    return render(request, "App1/Vendedores.html")

def Productos(request):
    return render(request, "App1/Productos.html")

def RecursosHumanos(request):
    return render(request, "App1/RecursosHumanos.html")