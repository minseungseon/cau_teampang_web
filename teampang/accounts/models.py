from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db.models.signals import post_save#커스텀유저
from django.dispatch import receiver#커스텀유저



#여기서부터 상속 커스텀 유저 모델
#from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
#from django.db import models

class UserManager(BaseUserManager):
    
    use_in_migrations = True    
    
    def create_user(self, email, nickname, birthdate, univ, major, gender, profile_photo, password=None):        
        
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

    birthdate = models.DateField(default=None, blank=True)
    #선택 변수 선언?
    CAU = '중앙대'
    OTHER = '타 대학'
    CLOSED = '비공개'
    SOFT = '솦트'
    YOUNG = '융공'
    BUILD = '건공'
    MAN = '남'
    WOMAN = '여'

    UNIV_CHOICES = (
        (CAU, '중앙대'),
        (OTHER, '타 대학'),
        (CLOSED, '비공개'),
    )
    univ = models.CharField(max_length=10, choices=UNIV_CHOICES, default=CLOSED, blank=True)
    MAJOR_CHOICES = (
        (SOFT, '솦트'),
        (YOUNG, '융공'),
        (BUILD, '건공'),
        (CLOSED, '비공개'),
    )
    major = models.CharField(max_length=10, choices=MAJOR_CHOICES, default=CLOSED, blank=True)
    GENDER_CHOICES = (
        (CLOSED, '비공개'),
        (MAN, '남'),
        (WOMAN, '여'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=None, blank=True)
    profile_photo = models.ImageField(default=None, null=True, blank=True)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'nickname'    
    REQUIRED_FIELDS = ['email']