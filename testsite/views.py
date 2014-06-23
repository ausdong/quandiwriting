from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm

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
	return render(request, 'testsite/submit.html')

		
def pwchangedone(request):
	return render(request, 'testsite/password_change_done.html')
		
	
def services(request):
	return render(request, 'testsite/services.html')