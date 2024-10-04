from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("Productos/",views.Productos,name="Productos"),
    path("Proveedores/",views.Proveedores,name="Proveedores"),
    path("Empleados/",views.Empleados,name="Empleados"),
    path("Clientes/",views.index,name="Clientes"),

]
