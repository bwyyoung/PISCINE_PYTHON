from django.db import models
from django.contrib.auth import get_user_model

class Tip(models.Model):

    contenu = models.TextField()
    auteur = models.ForeignKey(get_user_model(), related_name="tips")
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(get_user_model(), related_name="upvotes")
    downvotes = models.ManyToManyField(get_user_model(), related_name="downvotes")

    class Meta:
        permissions = (
            ("downvote_tip", "Can downvote tips"),
        )
