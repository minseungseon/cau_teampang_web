from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

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