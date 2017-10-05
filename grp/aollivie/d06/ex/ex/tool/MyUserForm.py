from django import forms
from django.contrib import auth
from ..models import MyUser

class MyUserForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100, required=True)
    password = forms.CharField(label='Your password', max_length=100, required=True, widget=forms.PasswordInput)
    password_check = forms.CharField(label='Your password again', max_length=100, required=True, widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(MyUserForm, self).is_valid()
        if not valid:
            return valid
        if self.cleaned_data['password'] != self.cleaned_data['password_check']:
            return 2
        try:
            user = MyUser.objects.get(username=self.cleaned_data['username'])
        except MyUser.DoesNotExist:
            return 0
        return 1
