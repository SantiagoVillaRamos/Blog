from django.urls import path
from .views import RegisterView, UserView, UserUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/user', UserView.as_view(), name='user'),
    path('auth/user/update', UserUpdateView.as_view(), name='user_update'),
    # JWT authentication endpoints
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]