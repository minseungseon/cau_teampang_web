from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meeting.urls')),
    path("api/", include("account.urls")),
    path("api/auth", include("knox.urls")),
] 