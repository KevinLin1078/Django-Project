from django.db import models


class PostManager(models.Manager):
	def get_likes(self, count):
		self.filter(like__lt=count)

	