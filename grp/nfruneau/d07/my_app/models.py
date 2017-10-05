from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=64)
	author = models.ForeignKey(User, null=False)
	created = models.DateTimeField(default=datetime.now,null=False)
	synopsis = models.CharField(max_length=312, null=False)
	content = models.TextField(null=False)

	def __str__(self):
		return self.title

class UserFavouriteArticle(models.Model):
	user = models.ForeignKey(User, null=False)
	article = models.ForeignKey('Article', null=False)

	def __str__(self):
		return article.title
