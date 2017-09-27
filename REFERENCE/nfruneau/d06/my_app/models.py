from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

class Tip(models.Model):
	content = models.TextField(null=True)
	author = models.CharField(max_length=100)
	postdate = models.DateTimeField(default=datetime.now)
