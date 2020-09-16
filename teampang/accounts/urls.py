from rest_framework.routers import DefaultRouter#router.py 정의해서 묶어서 import 하기
from django.urls import path, include
from accounts import views
from accounts.views import RegisterAPI, LoginAPI #위에서 import 했었는데 이거 추가 안하니까 오류나네요..?
from knox import views as knox_views#로그인/로그아웃 기능

router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),#회원가입, class일때는 as_view로 하자.
    path('api/login/', LoginAPI.as_view(), name='login'),#로그인
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),#로그아웃
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),#모두로그아웃
]