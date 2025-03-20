from post.models import Post
from post.api.serializer import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from post.api.permissions import IsAdminOrReadOnly

class PostApiViewSet(viewsets.ModelViewSet):
    # filtrar por publicados
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    # filtrar por categorias y por slug
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','category__slug']
    # filterset_fields = ['category']
    permission_classes = [IsAdminOrReadOnly]