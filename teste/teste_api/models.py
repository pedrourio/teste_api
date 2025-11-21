from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(
        max_length=100, 
        default='Sem título'
    )
    description = models.TextField(default="Campo vazio")
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User",
        related_name = "posts",
        on_delete=models.CASCADE
        )
    
    class Meta:
        ordering = ["created", "last_edit"]

    def __str__(self):
        return self.title
    
