from rest_framework import status
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

# clase registro de usuario
class RegisterView(APIView):
    # metodo post para registrar nuevos usuarios
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# clase que obtiene los datos de un usuario
class UserView(APIView):
    # permisos, solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [IsAuthenticated]
    
    # metodo get para obtener los datos de un usuario
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# vista que actualiza los datos de un usuario
class UserUpdateView(APIView):
    # permisos, solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [IsAuthenticated]
    
    # metodo put para actualizar los datos de un usuario
    def put(self, request):
        # obtenemos el usuario autenticado actual
        user = User.objects.get(id=request.user.id)
        # pasamos los datos actuales del usuario y los datos nuevos datos del usuario
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)