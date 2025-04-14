from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# clase encargada de registrar un nuevo usuario
class RegisterView(APIView):
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

# clase encargada de devolver los datos del usuario  
class UserView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    # devolver los datos del usuario
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# clase de actualizar los datos del usuario
class UserUpdateView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # actualizar los datos del usuario
    def put(self, request):
        # verificar si el usuario existe
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
