from django.contrib import admin
from art_gallery.models import UserProfileInfo, Category,GalleryModel

# Register your models here.

# register Category, UserProfile and Gallery Models
admin.site.register(UserProfileInfo)
admin.site.register(Category)
admin.site.register(GalleryModel)