from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 업로더(작성자) 연결
    content = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='boards/', blank=True, null=True)  # 'boards/' 폴더에 저장
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.created_at.strftime('%Y-%m-%d')}"
