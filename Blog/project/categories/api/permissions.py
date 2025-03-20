from rest_framework.permissions import BasePermission

# clase que permite a los usuarios que sean administradores puedan realizar acciones en la API de categorias o puedan leer
class IsAdminOrReadOnly(BasePermission):
    # funcion que permite a los usuarios que sean administradores puedan realizar acciones en la API de categorias o puedan leer
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff