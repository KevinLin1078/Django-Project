from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import CustomUser
from .forms import LoginForm, SignUpForm

Users = get_user_model()
class Index(View):
	def get(self, request):
		return render(request, 'index.html',{})


class Register(APIView):
	permission_classes = (IsAuthenticated,) # Automatically authenticates user through ReSTful API
	
	def get(self, request):
		
		obj = Users.objects.filter(email='a@gmail.com')
		print('Added')
		return JsonResponse({'foo':'bar'})


class SignUp(View):

	def get(self, request):
		return render(request, 'signup.html',{'SignUpForm': SignUpForm() })

	def post(self, request):
		form = SignUpForm(request.POST)

		if form.is_valid():
			email, password, password2 = form.cleaned_data['email'], form.cleaned_data['password'], form.cleaned_data['password2']
			try:
				user = Users.objects.get(email=email)
			except Users.DoesNotExist:
				if password != password2: return HttpResponse("Passwords Do Not Match", status=405)
				form.save(commit=True)
				
				u = Users.objects.get(email=email)
				u.set_password(password)
				u.save()
				return HttpResponse("User Created", status=201)

			return HttpResponse("Email Already Exists", status=405)
		
		return HttpResponse("Invalid SignUp Form Input", status=402)



from django.contrib.auth import authenticate, login, logout # THIS USES 'from users.backends import UserBackend ' as default 
class Login(View):	

	def get(self, request):
		return render(request, 'login.html',{'LoginForm': LoginForm() })

	def post(self, request):
		form = LoginForm(request.POST) 	# Takes in form parameter

		if form.is_valid():
			email, password = form.cleaned_data['email'], form.cleaned_data['password']
			
			try:
				user = Users.objects.get(email=email)
			except Users.DoesNotExist:
				return HttpResponse("Http Login: Invalid Email", status=401)

			is_password = user.check_password(password)

			if is_password:
				valid_user = authenticate(request, username=email, password=password)
				login(request, valid_user) # login() sets request.user = valid_user  ALSO  # print(request.user)
				return HttpResponse("Http Login: Success", status=200)
			else:
				return HttpResponse("Http Login: Wrong Password", status=402)

		return HttpResponse("Http Login: Invalid Form Inputs", status=403)



class Logout(View):

	def post(self, request):
		logout(request) # sets request.user = None

