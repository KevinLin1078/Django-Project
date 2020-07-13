from django.db import models
from users.models import CustomUser 

# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
	description = models.TextField(blank=True)

	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
	comment =  models.TextField()

	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)


