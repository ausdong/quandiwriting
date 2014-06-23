from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from django.forms.extras.widgets import Select
from testsite.formatChecker import ContentTypeRestrictedFileField

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
		
WORD_COUNT_CHOICES = (('short', '600 words or less'), ('medium', '601-900 words'), ('long', '901-1500 words'))
ESSAY_TYPE_CHOICES = (('capp', 'College Application'), ('msapp', 'Medical School Application'), ('law', 'Law School'), ('mb', 'MBA'), ('grad', 'Graduate School'), ('cover', 'Cover Letter'), ('other', 'Other (please specify in comments!)'))

#form for submission
class SubmissionForm(forms.Form):
	word_count = forms.ChoiceField(choices = WORD_COUNT_CHOICES)
	type_of_essay = forms.ChoiceField(choices = ESSAY_TYPE_CHOICES)
	comments_or_special_requests = forms.CharField(required = False, widget = forms.Textarea)
	prompt = forms.CharField(required = False, widget = forms.Textarea)
	upload_file = forms.FileField()
	delivery = forms.BooleanField(required = False)