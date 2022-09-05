from django.contrib import admin
from .models import Categoria, Tarea, Usuario

admin.site.register(Tarea)
admin.site.register(Usuario)
admin.site.register(Categoria)



