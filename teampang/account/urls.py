# api/urls.py
from django.urls import path
from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI, ProfileUpdateAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/profile/<int:user_pk>/update/", ProfileUpdateAPI.as_view()),
]