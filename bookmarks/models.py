from django.contrib.auth import get_user_model
from django.db import models

from bookmark_collections.models import Collections
from .choices import UrlTypeChoices

User = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    collections = models.ManyToManyField(Collections, 'bookmarks', blank=True)

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    url = models.URLField()
    url_type = models.CharField(max_length=32, choices=UrlTypeChoices.choices, default=UrlTypeChoices.website)
    image = models.ImageField(upload_to='images/bookmarks/%Y/%m/%d', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
