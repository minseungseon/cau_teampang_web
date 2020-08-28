from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save#커스텀유저
from django.dispatch import receiver#커스텀유저

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField() #여기에 넣고 싶은 정보 추가


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

class Account(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to="images")
    nickname = models.CharField(max_length = 20)
    birthdate = models.DateField(null=True, blank=True) #DB 레벨과 application 레벨에서 비어있어도 괜찮다는 의미
#    univ = models.NullBooleanField(default="대학")
#    major = models.NullBooleanField(default="학과")
#    profile_photo = models.ImageField(upload_to="images")
#    gender = models.NullBooleanField(default="성별")'''



class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    like = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()