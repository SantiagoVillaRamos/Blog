from rest_framework.permissions import BasePermission

# permisos personalizados para la api de post
# clase que maneja los permisos, si el usuario es admin puede hacer cualquier cosa
# si no es admin solo puede leer
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff