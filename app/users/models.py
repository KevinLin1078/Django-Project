from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
	objects = CustomUserManager()

	username = models.CharField(max_length=254, unique=True, default=None)
	email = models.EmailField(max_length=254, unique=True)
	
	two= models.CharField(max_length=254, unique=True, default=None)

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']