from django.urls import path
from App1.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('Clientes/', Clientes, name="Cursos"),
    path('Vendedores/', Vendedores, name="Vendedores"),
    path('Productos/', Productos, name="Productos"),
    path('RecursosHumanos/', RecursosHumanos, name="RecursosHumanos"),
]