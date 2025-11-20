from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField
    description = models.TextField
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ["created", "last_edit"]