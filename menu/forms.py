from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SigninForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
		]
		labels = {
				'username':'Usuario',
				'first_name':'Nombre',
				'last_name':'Apellido',
				'email':'Correo',
		}