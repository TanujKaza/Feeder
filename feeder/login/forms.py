from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.core.validators import validate_email

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class UserForm(ModelForm):
	username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	email = forms.EmailField(label="Email", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
	password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
	confirm_password = forms.CharField(label="Confirm Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'confirm_password'}))

	def clean(self): 
		if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['confirm_password']: 
				raise forms.ValidationError(_("Passwords do not match each other"))

		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError(_("Username is already used"))

		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError(_("Email Address is already used"))

		return self.cleaned_data

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'confirm_password')