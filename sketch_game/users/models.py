from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import logout
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, default='', blank=True)
    email = models.EmailField(max_length=255, unique=True, default='', blank=True)
    # avatar = models.ImageField(upload_to='images/') # not needed upon creation

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects= CustomUserManager()
    USERNAME_FIELD = 'username' 
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["email"] # username and password not included bc will always be req.

    class Meta:
        verbose_name='CustomUser'
        verbose_name_plural='CustomUsers'

    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    # will get to this later
    # def get_avatar(self):
    #     return self.avatar