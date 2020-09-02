from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
#from .models import Profile

#class ProfileInline(admin.StackedInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = "profile"


#class UserAdmin(BaseUserAdmin):
#    inlines = (ProfileInline,)


#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

#여기부터 커스텀 유저 모델
from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'nickname',
        'email',
        'date_joined',
    )

    list_display_links = (
        'nickname',
        'email',
    )