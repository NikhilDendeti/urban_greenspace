from django.urls import path
from .views import get_user_details, register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', get_user_details),
    path('register/', register_user),
]