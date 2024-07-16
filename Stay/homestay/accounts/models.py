from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Permission
from django.db import models
from datetime import datetime
from django.db.models.fields import *
from django.utils.translation import gettext_lazy as _

class CustomuserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        user.user_permissions.set(Permission.objects.all())
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customuser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    contactnumber = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomuserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    def get_user_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()
