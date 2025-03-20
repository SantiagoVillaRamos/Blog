from django.db import models
from users.models import User
from post.models import Post
# Create your models here.
class Comment(models.Model):
    content = models.TextField(verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Publicación', null=True)
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    
        