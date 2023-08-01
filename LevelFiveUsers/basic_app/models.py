from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # additional field to add :
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return  self.user.username

class ContactUsModel(models.Model):
    first_name = models.CharField(max_length=160)
    last_name  = models.CharField(max_length=160)
    email      = models.EmailField(max_length=200, blank=False, unique=True)
    desc       = models.TextField(blank=True)