from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import User as UserModel

User: type[UserModel] = get_user_model()


class Collection(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
