from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register(r'meetingCreates', views.MeetingCreateViewSet)
router.register(r'meetingInputs', views.MeetingInputViewSet)
router.register(r'meetingTimes', views.MeetingTimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    oa( '///' as_view(sdfsdfsd). , dsfjzklfsd)
]