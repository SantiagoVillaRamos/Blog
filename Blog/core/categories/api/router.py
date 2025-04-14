from .views import CategoryApiViewSet
from rest_framework.routers import DefaultRouter    

router_categories = DefaultRouter()
router_categories.register(prefix='categories', basename='categories', viewset=CategoryApiViewSet)

