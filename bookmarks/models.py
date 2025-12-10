from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import User as UserModel
from bookmark_collections.models import Collection
from core.enums.choices import UrlTypeChoices

User: type[UserModel] = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    collections = models.ManyToManyField(Collection, 'bookmarks', blank=True)

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    url = models.URLField()
    url_type = models.CharField(max_length=32, choices=UrlTypeChoices.choices, default=UrlTypeChoices.website)
    image = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
