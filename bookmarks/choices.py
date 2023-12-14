from django.db import models


class UrlTypeChoices(models.TextChoices):
    website = 'website'
    book = 'book'
    article = 'article'
    music = 'music'
    video = 'video'
