from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from login.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from main.models import *

user = authenticate(username='john', password='secret')

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
def register1(request,user_id):
	passw = str(random.randint(100000,1000000))
	user = User.objects.create_user(username=user_id,
                                 email='jlennon@beatles.com',
                                 password=passw)
	user.save()
	user = authenticate(username=user_id, password=passw)
	if user is not None:
		return HttpResponseRedirect(reverse('/home/'))

def reason(request):
	return render(request,"login/reason.html")

def privacy(request):
	return render(request,"login/privacy.html")

def terms(request):
	return render(request,"login/terms.html")

def about(request):
	return render(request,"login/about.html")

@csrf_exempt
def authenticate(request):
	if request.method == 'POST':
		incoming_rollno=request.POST.get('roll_num')
		incoming_password=request.POST.get('password')
		student = Student.objects.filter(roll_number=incoming_rollno,password=incoming_password)
		exist = False
		if student:
			exist = True
			
		if exist:
			return HttpResponse("True")
		else:
			return HttpResponse("False")
	else:
		return HttpResponse("")
		

