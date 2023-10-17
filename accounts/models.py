from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager,PermissionsMixin

  
class CustomBaseUserManager(BaseUserManager):
    def normalize_mobile(self,mobile):
        return ''.join(filter(str.isdigit,mobile))
    
    def create_user(self, mobile, password, **extra_fields):
        if not mobile:
            raise ValueError('The given mobile number must be set')
        email = self.normalize_mobile(mobile)
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(mobile, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    id_call = models.CharField(max_length=11)
    full_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    username  = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()

    def __str__(self):
        return self.mobile