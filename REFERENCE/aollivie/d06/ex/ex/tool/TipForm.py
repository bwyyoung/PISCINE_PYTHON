from django import forms
from django.contrib import auth
from ..models import Tip

class TipForm(forms.ModelForm):
    # contenu = forms.CharField(required=True, widget=forms.Textarea)
    class Meta:
        model = Tip
        exclude = ('auteur', 'upvotes', 'downvotes',)
        fields = ['contenu',]
