from django import forms
from .models import Article
class PublishForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'created', 'synopsis',)
        fields = ['title', 'content',]
    # submit_button = '<type="input value="Submit">'
