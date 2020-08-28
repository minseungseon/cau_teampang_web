from django.db import models
from django.conf import settings


class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField() #여기에 넣고 싶은 정보 추가

class Profile(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to="images")
#    nickname = models.CharField(max_length = 20)
#    birthdate = models.DateField(null=True, blank=True) #DB 레벨과 application 레벨에서 비어있어도 괜찮다는 의미
#    univ = models.NullBooleanField(default="대학")
#    major = models.NullBooleanField(default="학과")
#    profile_photo = models.ImageField(upload_to="images")
#    gender = models.NullBooleanField(default="성별")'''


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")