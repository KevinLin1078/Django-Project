from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# Customize authenticate for Django
# View "django.contrib.auth.backends" for more info on class interface
class UserAuthentication(BaseBackend):
	#This Authentication backend works
	def authenticate(self, **kwargs ): # **kwarg = (email, password)
		Users = get_user_model()
		
		try:
			user = Users.objects.get(email=kwargs['email'])
		except Users.DoesNotExist:
			return None # return None if email doesnt exist
		
		return user 