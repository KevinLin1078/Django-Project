from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

# from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .forms import LoginForm

from .models import CustomUser

class Register(APIView):
	permission_classes = (IsAuthenticated,) # Automatically authenticates user through ReSTful API
	
	def get(self, request):
		Users = get_user_model()
		obj = Users.objects.filter(email='a@gmail.com')
		print('Added')
		return JsonResponse({'foo':'bar'})



from .backends import UserAuthentication 
class Login(View):	
	#Dont initialize models here, not good for application. WILL CAUSE ERRORS

	def get(self, request):
		form = LoginForm() 				# This form contains 2 types of forms: RESTful and HTTP
		return render(request, 'login.html',{'LoginForm': form})

	def post(self, request):
		Users, form = get_user_model(), LoginForm(request.POST) 	# Takes in form parameter

		if form.is_valid():
			email, password = form.cleaned_data['email'], form.cleaned_data['password']
			user = Users.objects.get(email=email)
			is_password = user.check_password(password)

			if is_password:
				print('------Is password correct?-------- ', is_password)
				request.user = UserAuthentication.authenticate(self, email=email, password=password)
				
				return HttpResponse("Good Http Session Login ", status=200)



		return HttpResponse("Bad Login", status=405)



class Logout(View):
	permission_classes = (IsAuthenticated,)
	def post(self, request):
		pass

