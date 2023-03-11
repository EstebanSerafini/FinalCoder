from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null = True, blank = True)
    #Establecer relacion entre usuario y post. Si borramos el autor se borra en cascada todos los posts del autor.
    autor=models.ForeignKey(User, on_delete = models.CASCADE)
    #relacion varios a varios
    categorias=models.ManyToManyField(Categoria)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.titulo
    