from django import forms
from django.contrib.auth.models import User
from .models import *

class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']

		widgets = {
		'password': forms.PasswordInput(),
		'email': forms.EmailInput(),
		}
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(UserSignUp, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['email'].required = True
		self.fields['first_name'].required = True
	

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
