from django.db import models

# Create your models here.

# clase para la tabla de categorias
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    slug = models.SlugField(max_length=255,verbose_name='Slug', unique=True)
    published = models.BooleanField(verbose_name='Publicado', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created_at']

    def __str__(self):
        return self.title