from django import forms

PROVINCIAS_ARGENTINAS = (
    ('Buenos Aires', 'Buenos Aires'),
    ('C.A.B.A.', 'C.A.B.A.'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucumán'),
)

class form_RegistrarCliente(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=100, widget=forms.Select(choices=PROVINCIAS_ARGENTINAS),initial="Buenos Aires")
    CUIT = forms.IntegerField()
    email = forms.EmailField()

class form_RegistrarVendedor(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    provincia=forms.CharField(max_length=100, widget=forms.Select(choices=PROVINCIAS_ARGENTINAS),initial="Buenos Aires")
    CUIT=forms.IntegerField()
    email=forms.EmailField()

class form_RegistrarProducto(forms.Form):
    descripcion=forms.CharField(max_length=40)
    unidad=forms.CharField(max_length=5)  #kg,m,bolsa,caja,etc
    precio_unit=forms.FloatField()
    stock=forms.FloatField()
    exento=forms.BooleanField()  #Si el producto tiene eximición impositiva o no. 21 vs 10,5.

class form_RegistrarCandidato(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    CUIT=forms.IntegerField()
    email=forms.EmailField()
    descripcion=forms.CharField(max_length=100)
    CV=forms.FileField()