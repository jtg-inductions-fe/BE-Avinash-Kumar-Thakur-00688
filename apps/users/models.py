from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model where email is used as the
    identifier instead of username
    """

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('USER', 'User')
    ]

    username = None
    """Remove username field from user"""
    email = models.EmailField(unique=True)
    """Email of the user, it must be unique"""
    name = models.CharField(max_length=150)
    """The name of the user"""
    phone_number = models.CharField(max_length=10, unique=True)
    """Phone number of the user"""
    avatar = models.ImageField(
        upload_to='users/avatars/', null=True, blank=True)
    """Profile picture of the user"""
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='USER')
    is_active = models.BooleanField(default=True)
    """State whether user is active or not"""
    is_staff = models.BooleanField(default=False)
    """Whether user can access django admin site"""

    objects = UserManager()
    """Custom manager for creating user and superuser"""

    USERNAME_FIELD = 'email'
    """Field used as the unique identifier"""
    REQUIRED_FIELDS = ['phone_number', 'name']
    """Fields required while creating superuser"""
