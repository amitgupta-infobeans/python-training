from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional field to add :
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return  self.user.username

# Category Model
class Category(models.Model):
    
    name         = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index', kwargs={'pk':self.pk})


# Galery Model
class GalleryModel(models.Model):

    desc            = models.TextField()
    gallery_img     = models.ImageField(upload_to='gallery', blank=False)
    categoryid      = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    userid          = models.ForeignKey(User, related_name='user', null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('art_gallery:my_gallery')
    
    def __str__(self):
        return self.desc
    
    


