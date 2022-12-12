from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

