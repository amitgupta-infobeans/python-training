from typing import Any, Dict
from django import forms
from django.core import validators


# Validation for name field. It sholuld be start with z.
def check_name_startwithZ(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should be start from z")
    

class FormName(forms.Form):

    name  = forms.CharField(validators=[check_name_startwithZ])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email again:")
    text  = forms.CharField(widget=forms.Textarea)
    # for validation.... we add botcatcher so that
    # No one can edit the botcatcher input hidden field.
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput, 
                                 validators=[validators.MaxLengthValidator(0)]
                                )

    # check the email validation...
    def clean(self):
        all_clear_data = super().clean()
        email = all_clear_data['email']
        vemail = all_clear_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure both email should same..")
        
