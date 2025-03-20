from rest_framework import serializers
from post.models import Post
# importamos los serializadores de los modelos relacionados
from users.api.serializers import UserSerializer
from categories.api.serializer import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
        
        