from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion
    
class Tarea(models.Model):
    usuario = models.ForeignKey(Usuario,null=False, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    # le defino una clase meta para establecer el orden de como quiero que se ordenen en la base
    class Meta:
        ordering = ['completo']
        
    