from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


from django.contrib.auth import get_user_model


class Register(View):
	Users = get_user_model()

	def get(self, request):
		users = get_user_model()
		#user1 = users.objects.create_superuser(email='test0@gmail.com', password='test0')

		obj = users.objects.all()
		print(len(obj))
		print('Added')
		return HttpResponse('<html>123 </html>')


class Login(View):
	Users = get_user_model()

	def get(self, request):
		pass

	def post(self, request):
		pass



class Logout(View):
	def post(self, request):
		pass


class Delete(View):
	Users = get_user_model()

	def get(self, request):
		Users = Users.objects.all().delete()

	def post(self, request):
		pass

