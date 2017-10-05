from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    def presentation(self):
        print('hello i am a custom user')

class Tip(models.Model):
    contenu = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=128, null=False)
    upvotes = models.TextField(null=True)
    downvotes = models.TextField(null=True)
