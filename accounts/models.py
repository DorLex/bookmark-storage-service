from django.contrib.auth.models import AbstractUser
from django.db import models

from .manegers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        validators=[AbstractUser.username_validator]
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
