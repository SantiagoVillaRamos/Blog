from rest_framework.routers import DefaultRouter
from comments.api.views import CommentViewSet

router_comment = DefaultRouter()
router_comment.register(prefix='comments', basename='comments', viewset=CommentViewSet)