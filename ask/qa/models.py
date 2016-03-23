from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField
	added_at = models.DataTimeField
	rating = models.IntegerField
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
	text = models.TextField
	added_at = models.DataTimeField
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
		
# Create your models here.
