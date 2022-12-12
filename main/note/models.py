from django.db import models
from django.contrib.models.auth import User
# Create your models here.
class Note(models.Model):
    owner = User
    title = models.CharField(max_length=250)
    content = models.TextField()

