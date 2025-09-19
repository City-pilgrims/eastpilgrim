from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class ContentBlock(models.Model):
    TEXT = 'text'
    IMAGE = 'image'
    BLOCK_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    ]

    content = models.ForeignKey(Content, related_name='blocks', on_delete=models.CASCADE)
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='content_blocks/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']