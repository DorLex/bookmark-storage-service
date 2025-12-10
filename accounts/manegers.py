from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def _create_user(self, email: str, password: str, **extra_fields: Any) -> AbstractUser:
        if not email:
            raise ValueError('email должен быть передан')

        email: str = self.normalize_email(email)
        user: AbstractUser = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email: str, password: str | None = None, **extra_fields: Any) -> AbstractUser:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str | None = None, **extra_fields: Any) -> AbstractUser:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
