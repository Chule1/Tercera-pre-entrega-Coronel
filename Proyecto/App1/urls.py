from django.urls import path
from App1.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('Clientes/', Clientes, name="Cursos"),
    path('Vendedores/', Vendedores, name="Vendedores"),
    path('Productos/', Productos, name="Productos"),
    path('Empty/', Empty, name="Empty"),
    path('RecursosHumanos/', RecursosHumanos, name="RecursosHumanos"),
    path('Clientes/Registrar/', RegistrarCliente, name="RegistrarCliente"),
]