from rest_framework.viewsets import ModelViewSet
from categories.models import Categorie
from . serializer import CategorieSerializer
from .permisions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAdminOrReadOnly]
    
