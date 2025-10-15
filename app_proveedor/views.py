

from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

# 1. HOME/MENÚ
def index(request):
    """Muestra el menú principal de la app_proveedor (index.html)."""
    return render(request, 'index.html') 

# 2. READ (Listar - La tabla CRUD)
def listar_proveedores(request):
    """Obtiene todos los proveedores y los muestra en la tabla."""
    proveedores = Proveedor.objects.all()
    return render(request, 'read_proveedor.html', {'proveedores': proveedores})

# 3. CREATE (Agregar)
def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre=request.POST['nombre'],
            ap_paterno=request.POST['ap_paterno'],
            ap_materno=request.POST['ap_materno'],
            categoria=request.POST['categoria'],
            contacto=request.POST['contacto']
        )
        return redirect('read_proveedor') #  Redirige al nuevo listado
    
    return render(request, 'update_proveedor.html')

# 4. UPDATE (Editar)
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id) 
    
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.ap_paterno = request.POST['ap_paterno']
        proveedor.ap_materno = request.POST['ap_materno']
        proveedor.categoria = request.POST['categoria']
        proveedor.contacto = request.POST['contacto']
        
        proveedor.save() 
        return redirect('read_proveedor') #  Redirige al nuevo listado
    
    return render(request, 'update_proveedor.html', {'proveedor': proveedor})

# 5. DELETE (Borrar)
def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    
    if request.method == 'POST':
        proveedor.delete() 
        return redirect('read_proveedor') #  Redirige al nuevo listado
        
    return render(request, 'delete_proveedor.html', {'proveedor': proveedor})