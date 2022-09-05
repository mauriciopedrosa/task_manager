from .models import Categoria, Tarea, Usuario
from django.shortcuts import render
from .forms import CategoriasForm, TareasForm, UsuariosForm
from django.db.models import Q
 
 
def home(request):
    return render(request, 'app_tareas/home.html') 
 
## ------------ VISTAS DE LISTA DE DATOS ----------- 
 
def tareas(request): 
    queryset = request.GET.get("buscar")   # veo si fue utilizado el buscar para filtrar
    
    lista_tareas = Tarea.objects.all()     # traigo todas las tareas 
    if queryset:                           # si queryset vino con datos filtro la lista 
        lista_tareas = Tarea.objects.filter(
            Q(titulo__icontains = queryset)  
        )
    return render(request, "app_tareas/tareas.html", {'tarea': lista_tareas})

def categorias(request):
    queryset = request.GET.get("buscar")     

    lista_categorias = Categoria.objects.all()
    if queryset:                            
        lista_categorias = Categoria.objects.filter(
            Q(descripcion__icontains = queryset)  
        )    
    return render(request, "app_tareas/categorias.html", {'categoria': lista_categorias})
  

def usuarios(request):
    queryset = request.GET.get("buscar")     
    
    lista_usuarios = Usuario.objects.all()    
    if queryset:                           
        lista_usuarios = Usuario.objects.filter(
            Q(nombre__icontains = queryset)  
        )        
    return render(request, "app_tareas/usuarios.html", {'usuario': lista_usuarios})
  
## ------------ VISTAS FORM CREACION ----------- 

def crear_tarea(request):
    data = {'form': TareasForm()} 
    
    if request.method == 'POST':
        formulario = TareasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tarea Creada"
        else:
            data["form"] = formulario
    return render(request, "app_tareas/form_tareas.html", data)
  

def crear_categoria(request):
    data = {'form': CategoriasForm()}
    
    if request.method == 'POST':
        formulario = CategoriasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Categoria Creada"
        else:
            data["form"] = formulario
    return render(request, "app_tareas/form_categorias.html", data)


def crear_usuario(request):
    data = {'form': UsuariosForm()}
    
    if request.method == 'POST':
        formulario = UsuariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario Creado"
        else:
            data["form"] = formulario
    return render(request, "app_tareas/form_usuarios.html", data)


##### ----------------- VISTAS DE BUSQUEDA ---------------------

