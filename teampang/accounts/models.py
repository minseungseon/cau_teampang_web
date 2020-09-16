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

    def create_superuser(self, email, nickname, univ, birthdate, major, gender, profile_photo, password=None):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,
            birthdate = birthdate,
            univ = univ,
            major = major,   
            gender = gender,
            profile_photo = profile_photo
        )

        user.set_password(password)


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

    birthdate = models.DateField(default=None, null=True, blank=True)
    #선택 변수 선언?
    CLOSED = '비공개'
    MAN = '남'
    WOMAN = '여'


    univ = models.CharField(max_length=10, default=CLOSED, null=True, blank=True)

    major = models.CharField(max_length=10, default=CLOSED, null=True, blank=True)

    GENDER_CHOICES = (
        (CLOSED, '비공개'),
        (MAN, '남'),
        (WOMAN, '여'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, default=None, blank=True)
    profile_photo = models.ImageField(default=None, null=True, blank=True)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'nickname'    
    REQUIRED_FIELDS = ['email', 'univ', 'major', 'gender', 'profile_photo', 'birthdate']