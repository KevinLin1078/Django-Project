from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import resolve, reverse





# python manage.py test users.testing.tests.TestAbstractUser

class TestAbstractUser(TestCase):
	users = get_user_model()
	
	@classmethod
	def setUp(cls):
		cls.user1 = cls.users.objects.create_user(email='alias@gmail.com', password='alias')
		cls.user2 = cls.users.objects.create_superuser(email='super@gmail.com', password='super')
		
	def test_user_data(self):
		self.assertEqual(self.user1.email, 'alias@gmail.com')
		self.assertEqual(self.user2.email, 'super@gmail.com')

	def test_get_login_page(self):
		login = resolve('/login/')
		response = self.client.get(reverse("users:login"))

		self.assertEqual(login.view_name, 'users:login')
		self.assertEqual(response.status_code, 200)

	def test_user_login(self):
		data = 	{"email": self.user1.email, 'password': 'alias' }
		
		response = self.client.post('/login/', data=data )
		self.assertEqual(response.status_code, 200)




