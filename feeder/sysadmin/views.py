from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from login.forms import LoginForm

def sysadmin(request):
	return render(request,'sysadmin/sysadmin.html',{'authentication_form': LoginForm})
