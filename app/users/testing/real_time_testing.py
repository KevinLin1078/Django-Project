import unittest
import requests



class LoginServerTesting(unittest.TestCase):
	
	LOGIN_URL = 'http://127.0.0.1:8000/login/'
	data =	{'email':'kevin@gmail.com' ,'password':'kevin'}
	
	def test_real_time_login(self):
		client = requests.session()

		response = client.get(self.LOGIN_URL)
		self.data['csrfmiddlewaretoken'] = client.cookies['csrftoken']

		r = client.post(self.LOGIN_URL, data=self.data, headers=dict(Referer=self.LOGIN_URL))
		self.assertEqual(r.status_code, 200)




if __name__ == '__main__':
	unittest.main()