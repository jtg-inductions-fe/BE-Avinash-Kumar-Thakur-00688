from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.users import manager as users_manager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model where email is used as the identifier instead of username
    """

    ROLE_CHOICES = [("ADMIN", "Admin"), ("USER", "User")]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField()
    avatar = CloudinaryField("avatar", folder="users/images/", null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="USER")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = users_manager.UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
