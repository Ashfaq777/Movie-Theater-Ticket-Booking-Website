from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100, blank = True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.CharField(max_length= 200, blank= True)

    def __str__(self):
        return f'{self.username}'    
