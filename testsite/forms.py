from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User

#validation for user creation
class UserForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField()
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=PasswordInput, max_length=50)
	
	def clean_username(self):
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(u'Username is already in use.')