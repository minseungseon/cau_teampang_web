from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meeting.urls')),
    path('', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),#오른쪽 위에 로그인/로그아웃 버튼 만들기
] 