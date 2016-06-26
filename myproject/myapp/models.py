from django.db import models
from django.utils import timezone

class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        published_date = models.DateTimeField(blank=True, null=True)
        thumbnail = models.TextField()

class Image(models.Model):
        post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
        image = models.FileField(upload_to='image/%Y/%m/%d')
        uploaded_date = models.DateTimeField(default=timezone.now)

# Create your models here.
