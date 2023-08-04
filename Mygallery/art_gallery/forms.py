from django import forms
from django.contrib.auth.models import User
from art_gallery.models import UserProfileInfo

# created user registration form using ModelForm
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


# To add extra field: profile_pic
class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('profile_pic',)