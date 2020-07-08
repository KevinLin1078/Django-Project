from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class CustomUser(AbstractUser):

	username = models.CharField(max_length=254, unique=True, default='none')
	email = models.EmailField(max_length=254, unique=True)
	

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = CustomUserManager()
	# authenticate = UserAuthentication()
