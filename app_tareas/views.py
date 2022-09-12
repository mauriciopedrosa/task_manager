from multiprocessing import context
from .models import Categoria, Tarea, Usuario
from django.shortcuts import render
# a trabajar las vistas por Clase:
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
 
 
def home(request):
    return render(request, 'app_tareas/home.html') 

class Logueo(LoginView):
    field = '__all__'
    redirect_authenticated_user: True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
## ------------ VISTAS TAREAS ----------- 

class ListaTareas(LoginRequiredMixin, ListView):
    
    model = Tarea
    context_object_name = 'tareas'
    
    
class DetalleTarea(LoginRequiredMixin,DetailView):
    
    model = Tarea
    context_object_name = 'tarea'
    
class CrearTarea(LoginRequiredMixin,CreateView):
    
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

class EditarTarea(LoginRequiredMixin,UpdateView):
    
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')
    
class EliminarTarea(LoginRequiredMixin,DeleteView):
    
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')    
    
    
 # ---------- VISTAS USUARIOS -------------
 
class ListaUsuarios(LoginRequiredMixin,ListView):
    
    model = Usuario
    context_object_name = 'usuarios'   
    
class DetalleUsuario(LoginRequiredMixin,DetailView):
    
    model = Usuario
    context_object_name = 'usuario'
    
class CrearUsuario(LoginRequiredMixin,CreateView):
    
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('usuarios')

class EditarUsuario(LoginRequiredMixin,UpdateView):
    
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('usuarios')
    
class EliminarUsuario(LoginRequiredMixin,DeleteView):
    
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy('usuarios')        
    
# ---------- VISTAS CATEGORIAS -------------
 
class ListaCategorias(LoginRequiredMixin,ListView):
    
    model = Categoria
    context_object_name = 'categorias'   
    
class DetalleCategoria(LoginRequiredMixin,DetailView):
    
    model = Categoria
    context_object_name = 'categoria'
    
class CrearCategoria(LoginRequiredMixin,CreateView):
    
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('categorias')

class EditarCategoria(LoginRequiredMixin,UpdateView):
    
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('categorias')
    
class EliminarCategoria(LoginRequiredMixin,DeleteView):
    
    model = Categoria
    context_object_name = 'categoria'
    success_url = reverse_lazy('categorias')        
        
 