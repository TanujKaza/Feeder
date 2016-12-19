from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from login.forms import LoginForm

def sysadmin(request):
	return render(request,'sysadmin/sysadmin.html',{'authentication_form': LoginForm})

def privacy(request):
	return render(request,'sysadmin/privacy.html')

def reason(request):
	return render(request,'sysadmin/reason.html')

def terms(request):
	return render(request,'sysadmin/terms.html')

def about(request):
	return render(request,'sysadmin/about.html')

