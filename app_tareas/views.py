from .models import Categoria, Operador, Tarea
from django.shortcuts import render, redirect
from django.contrib import  messages # el storage de messages esta definido en settings

# a trabajar las vistas por Clase:
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# vistas para login y seguridad
# importo de FORMS el custom que realice de userregisterform y se lo envio a la vista con el data
from app_tareas.forms import CustomUserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
# funciones que me van a permitir autenticar al usuario
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
 
 
def home(request):
    return render(request, 'app_tareas/home.html') 

def about(request):
    return render(request, 'app_tareas/about/about.html')
         


## ------------ VISTAS REGISTRACION ---------------

def registro(request):
    data = {
        'form':CustomUserRegisterForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Correcto.")
            return redirect(to='home')
        
    return render(request, 'registration/registro.html', data)
    
     

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


def tarea(request, usuario_id):
    user = User.objects.filter(id = usuario_id)
    tareas = Tarea.objects.filter(usuario_id = user[0])
    return render(request, "app_tareas/tareas/tarea_usuario.html", {'tareas': tareas, 'empleado': user[0]})
 
    
    
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
        
# ---------------- vista USERS ---------------
class ListaUsuarios(LoginRequiredMixin,ListView):
    
    model = User
    context_object_name = 'usuarios'   
    template_name = 'app_tareas/usuarios/lista_usuarios.html'       
    
    
class EditarUsuario(LoginRequiredMixin,UpdateView):
    
    model = User
    fields =  ['username','first_name', 'last_name'] 
    success_url = reverse_lazy('home')
    template_name = 'app_tareas/usuarios/form_usuario.html' 