from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm, SubmissionForm
from django.core.mail import send_mail

#home page
def index(request):
	return render(request, 'testsite/index.html')
	
#about us page
def about(request):
	return render(request, 'testsite/About.html')
	
#registration page
def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			first = form.cleaned_data['first_name']
			last = form.cleaned_data['last_name']
			newuser = User.objects.create_user(name, form.cleaned_data['email'], pw)
			newuser.last_name = last
			newuser.first_name = first
			newuser.save() 
			user = authenticate(username=name, password=pw)
			login(request, user)
			return HttpResponseRedirect(request.GET['next'])
	else:
		form = UserForm()
	return render(request, 'testsite/register.html', {'form':form})
	
#profile page
def profile(request):
		return render(request, 'testsite/profile.html')
	
@login_required()	
def submission(request):
	if request.method == 'POST':
		form = SubmissionForm(request.POST, request.FILES)
		if form.is_valid():
			wcount = form.cleaned_data['word_count']
			essaytype = form.cleaned_data['type_of_essay']
			comment = form.cleaned_data['comments_or_special_requests']
			prompts = form.cleaned_data['prompt']
			document = form.cleaned_data['upload_file']
			fast = form.cleaned_data['delivery']
			newsubmission = submission.create(user = user.username, paid = False, count = wcount, type = essaytype, comments = comment, prompt = prompts, express = fast, attached_file = document)			
			newsubmission.save()
			return HttpResponseRedirect('/')
	else:
		form = SubmissionForm()
	return render(request, 'testsite/submit.html', {'form':form})

		
def pwchangedone(request):
	return render(request, 'testsite/password_change_done.html')
		
	
def services(request):
	return render(request, 'testsite/services.html')