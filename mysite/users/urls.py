from django.urls import path 
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView, UserActivationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('activate/<uidb64>/<token>/', UserActivationView.as_view(), name='user-activate')
]