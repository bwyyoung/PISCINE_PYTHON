from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Post(models.Model):
	title = models.CharField(max_length=64, unique=True, null=False)
	author = models.ForeignKey(AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
	content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True, null=False)

	def __str__(self):
		return self.title


class MyComment(models.Model):
	author = models.ForeignKey(AUTH_USER_MODEL, null=False)
	content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True, null=False)

	post_id = models.PositiveIntegerField()
	comment_id = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.content

