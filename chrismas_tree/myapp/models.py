from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 600)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)