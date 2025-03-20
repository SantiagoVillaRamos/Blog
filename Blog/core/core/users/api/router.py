from django.urls import path
from .views import RegisterView, UserView, UserUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/user/me/', UserView.as_view(), name='user'),
    path('auth/user/update/', UserUpdateView.as_view(), name='update'),
]