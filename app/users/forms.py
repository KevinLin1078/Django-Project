from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
	email  = forms.EmailField(max_length=100, required = True)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)


class LoginForm2(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['email', 'password', 'username']
		exclude = []