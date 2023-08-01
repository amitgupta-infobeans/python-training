from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, ContactUsModel


class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')



class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')



class ContactUsForm(forms.ModelForm):

    class Meta():
        model = ContactUsModel
        fields = ('first_name', 'last_name', 'email', 'desc')



 



