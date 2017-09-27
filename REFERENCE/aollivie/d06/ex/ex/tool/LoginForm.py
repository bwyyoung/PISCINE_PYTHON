from django import forms
from django.contrib import auth
from ..models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100, required=True)
    password = forms.CharField(label='Your password', max_length=100, required=True, widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        if not valid:
            return valid
        print(self.cleaned_data['password'])
        return True
