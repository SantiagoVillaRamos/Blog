from django.db import models
from users.models import User
from categories.models import Categorie

class Posts(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    miniature = models.ImageField(upload_to='posts/images/', verobse_name='Miniatura')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    published = models.BooleanField(default=False, verbose_name='Publicado')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Usuario')
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, verbose_name='Categoría')