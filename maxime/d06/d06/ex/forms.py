from django import forms
from django.contrib.auth.models import User

class FormSign(forms.ModelForm):
	password_check = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ['username', 'password']
