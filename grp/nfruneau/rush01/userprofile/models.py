from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	description = models.TextField(max_length=500, default='', null=True)
	picture = models.ImageField(upload_to='files', null=True)



def create_profile(sender, **kwargs):
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = UserProfile(user=user)
		user_profile.save()
post_save.connect(create_profile, sender=User)