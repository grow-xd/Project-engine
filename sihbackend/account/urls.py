from django.urls import path
from .views import UserLogin, UserRegistrationView

urlpatterns = [
    path('api/login/', UserLogin.as_view(), name='login'),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
]
