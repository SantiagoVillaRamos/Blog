from rest_framework.permissions import BasePermission
from comments.models import Comment

# si eres el propietario podras hacer de todo o si no podras solo leer y crear
class IsOwnerOrReadCreateOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # sacar el id del comentario que esta intentando actualizar o eliminar
            id_comment = view.kwargs['pk']
            # hacer peticion a la base de datos de ese comentario
            comment = Comment.objects.get(pk=id_comment)
            # id del usuario que esta ejecutando la accion
            id_user = request.user.pk
            # obtener el id del propietario del comentario
            id_user_comment = comment.user_id
            # comparamos si el id del usuario que esta haciendo la peticion es el mismo que el id del usuario que creo el comentario, podra eliminarlo o actualizarlo
            if id_user == id_user_comment:
                return True
            # sino, no tendra permiso
            return False