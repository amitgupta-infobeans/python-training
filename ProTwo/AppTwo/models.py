from django.db import models

# Create your models here.
class UserModel(models.Model):
    
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    email      = models.EmailField(unique=True, max_length=215)

