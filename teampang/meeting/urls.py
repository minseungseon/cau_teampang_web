from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register(r'Plan', views.PlanViewSet)
router.register(r'DummyPlan', views.DummyPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]