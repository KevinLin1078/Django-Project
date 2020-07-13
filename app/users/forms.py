from django import forms
from .models import CustomUser
from django.utils.safestring import mark_safe


class LoginForm(forms.Form):
	email  = forms.EmailField(max_length=100, required = True)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)


class LoginForm2(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['email', 'password', 'username']
		exclude = []


class SignUpForm(forms.ModelForm):  
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True) 
	password2 = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True, label=mark_safe('Re-enter Password'))
	
	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs) 
		fields = self.fields