from rest_framework import serializers
from categories.models import Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id','title', 'slug', 'publised']
        