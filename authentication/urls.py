from django.urls import path
from . import views


urlpatterns = [
    path('register', views.RegistrationAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('profile', views.ProfileCreateAPIView.as_view(), name='profile'),
]
