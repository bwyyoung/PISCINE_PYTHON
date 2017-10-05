from django import forms
from django.contrib import auth
from .models import User, Tip

class SigninForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content',]
