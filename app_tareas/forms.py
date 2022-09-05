from django import forms
from .models import Categoria,  Tarea, Usuario

class TareasForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'        
        
class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields= '__all__'
        
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        
        