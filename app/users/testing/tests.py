from django.test import TestCase
from django.contrib.auth import get_user_model


class TestAbstractUser(TestCase):
	users = get_user_model()

	@classmethod
	def test_add_user(cls):
		cls.user1 = cls.users.objects.create_user(email='kevin@gmail.com', password='kevin')
		cls.user2 = cls.users.objects.create_superuser(email='super@gmail.com', password='super')

		
	def test_user_data(self):
		self.assertEqual(self.user1.email, 'kevin@gmail.com')
		self.assertFalse(self.user1.is_staff)
		
		self.assertTrue(self.user2.is_staff)



