from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin, User
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
#    username = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    #user_pk = models.IntegerField(blank=True)
#    email = models.EmailField(max_length=500, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
#    like = models.CharField(max_length=200, blank=True)
#    phone = models.CharField(max_length=200, blank=True)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance, user_pk=instance.id)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()



#여기서부터 상속 커스텀 유저 모델
#from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
#from django.db import models

class UserManager(BaseUserManager):
    
    use_in_migrations = True    
    
    def create_user(self, email, nickname, password=None):        
        
        if not email:            
            raise ValueError('must have user email')        
        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user
 
    def create_superuser(self, email, nickname,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user

class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'nickname'    
    REQUIRED_FIELDS = ['email']