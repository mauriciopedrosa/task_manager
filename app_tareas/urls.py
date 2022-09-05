from django.urls import path
from .views import categorias, crear_tarea, crear_usuario, home, tareas, crear_categoria, usuarios

urlpatterns = [
    path('', home, name ='home'),
    path('tareas', tareas, name ='tareas'),
    path('crear_categorias', crear_categoria, name ='crear_categorias'),    
    path('crear_usuarios', crear_usuario, name ='crear_usuarios'),  
    path('crear_tareas', crear_tarea, name ='crear_tareas'),           
    path('usuarios', usuarios, name ='usuarios'),     
    path('categorias', categorias, name ='categorias'),      
]
