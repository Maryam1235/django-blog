from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number=models.CharField(max_length=10)
    image=models.ImageField(upload_to="users/" ,null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username
    
class Feed(models.Model):   
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/")

    def __str__(self) -> str:
        return f"{self.author.username} {self.created_at}"
    
class Comment(models.Model):
    feed=models.ForeignKey(Feed,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self)->str:
        return f"{self.author.username} {self.created_at}"
    
        
