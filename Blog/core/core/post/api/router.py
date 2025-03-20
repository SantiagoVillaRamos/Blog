from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router_post = DefaultRouter()
router_post.register(prefix='posts', basename='posts', viewset=PostApiViewSet)