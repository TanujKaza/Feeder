from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from login.forms import UserForm
from django.contrib.auth.decorators import login_required

def register(request):
	success = False
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			login(request,user)
			success = True
	else:
		form = UserForm()
	return render(request, 'login/register.html', {'form': form, 'success': success})

def reason(request):
	return render(request,"login/reason.html")

def privacy(request):
	return render(request,"login/privacy.html")

def terms(request):
	return render(request,"login/terms.html")

def about(request):
	return render(request,"login/about.html")


