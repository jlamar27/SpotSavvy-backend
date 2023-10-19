from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    location = models.CharField(max_length=100)
        
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username