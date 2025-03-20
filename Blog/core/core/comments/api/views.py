from comments.models import Comment
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import CommentSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadCreateOnly


class CommentViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # añadir filtro por fecha de creación
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post']
