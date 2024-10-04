from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def Productos(request):
    return render(request,"Productos.html")

def Proveedores(request):
    return render(request,"Proveedores.html")

def Empleados(request):
    return render(request,"Empleados.html")

def Clientes(request):
    return render(request,"Clientes.html")



