from rest_framework.permissions import BasePermission

# clase para verificar permisos de admin o solo lectura
# Permisos para el admin o solo lectura
class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff