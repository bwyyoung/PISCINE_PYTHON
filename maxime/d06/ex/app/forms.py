from django import forms
from django.contrib.auth import get_user_model, authenticate
from .models import Tip

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
         model = get_user_model()
         fields = ['username', 'password',]

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def save(self):
        new_user = self.Meta.model.objects.create_user(
            self.cleaned_data['username'],
            None,
            self.cleaned_data['password']
        )
        return new_user


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def clean(self):
        u = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        if not u:
            raise forms.ValidationError('invalid username/password couple')
        else:
            self.cleaned_data['user'] = u

class TipForm(forms.ModelForm):

    class Meta:
        model = Tip
        fields = ['contenu',]
