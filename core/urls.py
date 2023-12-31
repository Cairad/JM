from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('indexapi/', indexapi, name="indexapi"),
    path('productos/', productos, name="productos"),
    path('perfil/', perfil, name="perfil"),
    path('segumiento/', seguimiento, name="seguimiento"),
    path('devolvercarrito/', devolvercarrito, name="devolvercarrito"),
    path('carrito/', carrito, name="carrito"),
    path('agregaralcarrito/<id>/', agregaralcarrito, name="agregaralcarrito"),
    path('eliminarcarrito/<id>/', eliminarcarrito, name="eliminarcarrito"),
    path('historial/', historial, name="historial"),
    path('suscribete/', agregarsus, name="suscribete"),
    path('subscrito/', subscrito, name="subscrito"),
    path('suscriptores/', suscriptores, name="suscriptores"),
    path('modificarsus/<id>/', modificarsus, name="modificarsus"),
    path('eliminarsus/<id>/', eliminarsus, name="eliminarsus"),
    path('crud/', crud, name="crud"),
    path('agregar/', agregar, name="agregar"),
    path('comprar_producto/<id>/', comprar_producto, name='comprar_producto'),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminarproducto/<id>/', eliminarproducto, name="eliminarproducto"),
    path('eliminar/<id>/', eliminar_producto, name="Del"),
    path('restar/<id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('agregar/<id>/', agregaralcarrito, name="Add"),
    path('api-auth/', include('rest_framework.urls')),
    path('guardar_en_historial/', guardar_en_historial, name='guardar_en_historial'),

]