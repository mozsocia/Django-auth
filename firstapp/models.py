from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)