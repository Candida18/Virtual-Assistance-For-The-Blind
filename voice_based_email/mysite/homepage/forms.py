from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields = ['email','password']
        widgets = {
        'email' : forms.EmailInput(),
        'password': forms.PasswordInput(),
        }
