from django.db import models

class Categorie(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Título')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    publised = models.BooleanField(default=True, verbose_name='Publicado')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ('-publised', 'title')
    
    def __str__(self):
        return self.title