from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		exclude = ['user']

class OrdenForm(ModelForm):
	class Meta:
		model = Orden
		fields = '__all__'

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CrearProveedorForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']