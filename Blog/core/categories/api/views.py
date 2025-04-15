from rest_framework.viewsets import ModelViewSet
from categories.models import Categorie
from django_filters.rest_framework import DjangoFilterBackend
from . serializer import CategorieSerializer
from .permisions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    
    serializer_class = CategorieSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Categorie.objects.filter(publised=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
