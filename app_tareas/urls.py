from django.urls import path
from .views import home, CrearCategoria, CrearUsuario, DetalleCategoria, DetalleUsuario, EditarCategoria, EditarUsuario, EliminarCategoria, EliminarUsuario, ListaCategorias, ListaUsuarios,  ListaTareas,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea, Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name ='home'), 
    path('login/', Logueo.as_view(), name ='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name ='logout'),    
    # --------- TAREAS ------------
    path('tareas/', ListaTareas.as_view(), name ='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name ='tarea'),
    path('crear_tarea/', CrearTarea.as_view(), name ='crear_tarea'),
    path('editar_tarea/<int:pk>', EditarTarea.as_view(), name ='editar_tarea'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name ='eliminar_tarea'), 
    #---------- USUARIOS -----------
    path('usuarios/', ListaUsuarios.as_view(), name ='usuarios'),       
    path('usuario/<int:pk>', DetalleUsuario.as_view(), name ='usuario'),           
    path('crear_usuario/', CrearUsuario.as_view(), name ='crear_usuario'),
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(), name ='editar_usuario'),
    path('eliminar_usuario/<int:pk>', EliminarUsuario.as_view(), name ='eliminar_usuario'), 
    #---------- CATEGORIAS -----------
    path('categorias/', ListaCategorias.as_view(), name ='categorias'),       
    path('categoria/<int:pk>', DetalleCategoria.as_view(), name ='categoria'),           
    path('crear_categoria/', CrearCategoria.as_view(), name ='crear_categoria'),
    path('editar_categoria/<int:pk>', EditarCategoria.as_view(), name ='editar_categoria'),
    path('eliminar_categoria/<int:pk>', EliminarCategoria.as_view(), name ='eliminar_categoria'),     
 
]
