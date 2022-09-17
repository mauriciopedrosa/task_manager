from .models import Categoria, Operador, Tarea
from django.shortcuts import render
# a trabajar las vistas por Clase:
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
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
    template_name = 'app_tareas/tareas/lista_tareas.html'    
    
    
class DetalleTarea(LoginRequiredMixin,DetailView):
    
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'app_tareas/tareas/detalle_tarea.html'        
    
class CrearTarea(LoginRequiredMixin,CreateView):
    
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')
    template_name = 'app_tareas/tareas/form_tarea.html'       

class EditarTarea(LoginRequiredMixin,UpdateView):
    
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')
    template_name = 'app_tareas/tareas/form_tarea.html'       
    
class EliminarTarea(LoginRequiredMixin,DeleteView):
    
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')   
    template_name = 'app_tareas/tareas/eliminar_tarea.html'       
     
    
    
 # ---------- VISTAS OPERADORES -------------
 
class ListaOperadores(LoginRequiredMixin,ListView):
    
    model = Operador
    context_object_name = 'operadores'   
    template_name = 'app_tareas/operadores/lista_operadores.html'
    
class DetalleOperador(LoginRequiredMixin,DetailView):
    
    model = Operador
    context_object_name = 'operador'
    template_name = 'app_tareas/operadores/detalle_operador.html'    
    
class CrearOperador(LoginRequiredMixin,CreateView):
    
    model = Operador
    fields = '__all__'
    success_url = reverse_lazy('operadores')
    template_name = 'app_tareas/operadores/form_operador.html'     

class EditarOperador(LoginRequiredMixin,UpdateView):
    
    model = Operador
    fields = '__all__' # podriamos pasar campo por campo = ['nombre','apellido'] y asi
    success_url = reverse_lazy('operadores')
    template_name = 'app_tareas/operadores/form_operador.html' 
    
class EliminarOperador(LoginRequiredMixin,DeleteView):
    
    model = Operador
    context_object_name = 'operador'
    success_url = reverse_lazy('operadores')   
    template_name = 'app_tareas/operadores/eliminar_operador.html'          
    
# ---------- VISTAS CATEGORIAS -------------
 
class ListaCategorias(LoginRequiredMixin,ListView):
    
    model = Categoria
    context_object_name = 'categorias'   
    template_name = 'app_tareas/categorias/lista_categorias.html'       
    
class DetalleCategoria(LoginRequiredMixin,DetailView):
    
    model = Categoria
    context_object_name = 'categoria'
    template_name = 'app_tareas/categorias/detalle_categoria.html'       
    
class CrearCategoria(LoginRequiredMixin,CreateView):
    
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('categorias')
    template_name = 'app_tareas/categorias/form_categoria.html'       

class EditarCategoria(LoginRequiredMixin,UpdateView):
    
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('categorias')
    template_name = 'app_tareas/categorias/form_categoria.html'      
    
class EliminarCategoria(LoginRequiredMixin,DeleteView):
    
    model = Categoria
    context_object_name = 'categoria'
    success_url = reverse_lazy('categorias')      
    template_name = 'app_tareas/categorias/eliminar_categoria.html'        
        
 