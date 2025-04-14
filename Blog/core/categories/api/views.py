from rest_framework.viewsets import ModelViewSet
from categories.models import Categorie
from . serializer import CategorieSerializer

class CategoryApiViewSet(ModelViewSet):
    
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
