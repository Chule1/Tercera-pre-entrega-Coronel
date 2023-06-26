from django.urls import path
from App1.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('Clientes/', Clientes, name="Cursos"),
    path('Vendedores/', Vendedores, name="Vendedores"),
    path('Productos/', Productos, name="Productos"),
    path('Empty/', Empty, name="Empty"),
    path('RecursosHumanos/', RecursosHumanos, name="RecursosHumanos"),
    path('RegistrarCliente/', RegistrarCliente, name="RegistrarCliente"),
    path('RegistrarVendedor/', RegistrarVendedor, name="RegistrarVendedor"),
    path('BuscarVendedor/', BuscarVendedor, name="BuscarVendedor"),
    path('aux_BuscarVendedor/', aux_BuscarVendedor, name="aux_BuscarVendedor"),
    path('RegistrarProducto/', RegistrarProducto, name="RegistrarProducto"),
    path('BuscarProducto/', BuscarProducto, name="BuscarProducto"),
]