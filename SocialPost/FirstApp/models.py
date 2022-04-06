from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Post = models.CharField(max_length=300)
    is_private = models.BooleanField()

    def __str__(self):
        return self.Title
