from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#크리스마스 장식 db
Decorations = (
    (0, 'decoration_1'),
    (1, 'decoration_2'),
    (2, 'decoration_3'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    decoration = models.IntegerField(default=0)  # 'decoration' 필드 추가

    def __str__(self):
        return self.title