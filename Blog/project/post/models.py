from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
# Create your models here.

# clase post que hereda de models.Model que es la clase base de todos los modelos de Django
# y que representa una tabla en la base de datos 
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    miniature = models.ImageField(upload_to='posts/img/', verbose_name='Miniatura', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    published = models.BooleanField(default=False, verbose_name='Publicado')
    user = models.ForeignKey(User, on_delete=SET_NULL,null=True, verbose_name='Usuario')
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, verbose_name='Categoría')
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        #ordering = ['-created_at']
        
    def __str__(self):
        return self.title