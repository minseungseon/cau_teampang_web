from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts import views

router = DefaultRouter()
router.register('profile_photo', views.Profile_PhotoSet)

urlpatterns = [
    path('', include(router.urls))
]