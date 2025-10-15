from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    # OPERACIONES CRUD
    path('listado/', views.listar_proveedores, name='read_proveedor'), 
    path('agregar/', views.agregar_proveedor, name='create_proveedor'), 
    path('editar/<int:id>/', views.editar_proveedor, name='update_proveedor'), 
    path('borrar/<int:id>/', views.borrar_proveedor, name='delete_proveedor'), 
]