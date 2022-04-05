from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):  # let's extend the Base User Manager

    def create_user(self, email, password=None, **extra_fields):
        # the **extra_fields makes our function more flexible
        # because every time we add a new fields to our user
        # it means that we do not have to add them in there.
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # With BaseUserManager comes the normalize_email
        # method. This makes the email in a naturally way
        # case insensitive.

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        # The lecturer puth in save 'self.__db' as parameer, but this
        # gives me some problems so I deleted it.
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # usually USERNAME_FIELD = username

    # After that, we add in app/settings.py the line
    # AUTH_USER_MODEL = 'core.User'
