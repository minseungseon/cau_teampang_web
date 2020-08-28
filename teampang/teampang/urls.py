"""teampang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls #accounts앱과 연결
from rest_framework import urls





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),#오른쪽 위에 로그인/로그아웃 버튼 만들기

    path("api/auth", include("knox.urls"))
]

# app : 기능별?! 우리 분업별? 
# account , kakaotalk api, 
