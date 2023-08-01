from django import forms
from AppTwo.models import UserModel


class NewUser(forms.ModelForm):

    # you can here custom validation for field first_name, last_name, email...

    class Meta:
        model = UserModel
        fields = '__all__'



