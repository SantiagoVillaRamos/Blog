from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializer import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True)# filtrar solo las categorías activ
    
    # añadir una propiedad que remplaza el id por el slug
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend] # añadir filtro por nombre de categoría 
    filterset_fields = ['title'] # añadir filtro por published de categoría
    