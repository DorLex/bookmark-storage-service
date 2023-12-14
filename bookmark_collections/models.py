from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Collections(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
