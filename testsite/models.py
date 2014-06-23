from django.db import models
from django.contrib.auth.models import User
from testsite.formatChecker import ContentTypeRestrictedFileField
# Create your models here.

class Submission(models.Model):
	user = models.OneToOneField(User)
	paid = models.BooleanField()
	count = models.CharField(max_length=20)
	type = models.CharField(max_length=40)
	comments = models.CharField(max_length=1000)
	prompt = models.CharField(max_length=1000)
	express = models.BooleanField()
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	attached_file = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['text/plain', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.oasis.opendocument.text'],max_upload_size=5242880)