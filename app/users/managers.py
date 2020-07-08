from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The Email must be set')
		
		user = self.model(email=email ,**extra_fields)
		user.set_password(password)
		user.save()
		print("User Created")
		
		return user
	
	def create_superuser(self,email,password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		return self.create_user(email, password, **extra_fields)


