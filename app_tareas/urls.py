from django.urls import path
from .views import EditarUsuario, ListaUsuarios, home, CrearCategoria, CrearOperador, DetalleCategoria, DetalleOperador, EditarCategoria, EditarOperador, EliminarCategoria, EliminarOperador, ListaCategorias, ListaOperadores,  ListaTareas,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea, Logueo, registro, tarea, about
from .views import home, CrearCategoria, CrearOperador, DetalleCategoria, DetalleOperador, EditarCategoria, EditarOperador, EliminarCategoria, EliminarOperador, ListaCategorias, ListaOperadores,  ListaTareas,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea, Logueo, registro, tarea, about
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name ='home'), 
    path('login/', Logueo.as_view(), name ='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name ='logout'),   
    path('registro/', registro, name ='registro'),   
    path('about/', about, name ='about'),   
    # --------- TAREAS ------------
    path('tareas/', ListaTareas.as_view(), name ='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name ='tarea'),
    path('crear_tarea/', CrearTarea.as_view(), name ='crear_tarea'),
    path('editar_tarea/<int:pk>', EditarTarea.as_view(), name ='editar_tarea'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name ='eliminar_tarea'), 
    path('tarea_usuario/<int:usuario_id>', tarea , name ='tarea_usuario'),
    
    #---------- OPERADORES -----------
    path('operadores/', ListaOperadores.as_view(), name ='operadores'),       
    path('operador/<int:pk>', DetalleOperador.as_view(), name ='operador'),           
    path('crear_operador/', CrearOperador.as_view(), name ='crear_operador'),
    path('editar_operador/<int:pk>', EditarOperador.as_view(), name ='editar_operador'),
    path('eliminar_operador/<int:pk>', EliminarOperador.as_view(), name ='eliminar_operador'), 
    #---------- CATEGORIAS -----------
    path('categorias/', ListaCategorias.as_view(), name ='categorias'),       
    path('categoria/<int:pk>', DetalleCategoria.as_view(), name ='categoria'),           
    path('crear_categoria/', CrearCategoria.as_view(), name ='crear_categoria'),
    path('editar_categoria/<int:pk>', EditarCategoria.as_view(), name ='editar_categoria'),
    path('eliminar_categoria/<int:pk>', EliminarCategoria.as_view(), name ='eliminar_categoria'),  
    
    # -----------USUARIOS ---------------
    path('usuarios/', ListaUsuarios.as_view(), name ='usuarios'),        
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(), name ='editar_usuario'),
]
