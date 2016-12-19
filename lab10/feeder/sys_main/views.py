from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,user_passes_test
from main.models import Course
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import CourseForm

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def sysmain(request):
	courses = Course.objects.all()
	context = {"courses" : courses}
	return render(request,"sys_main/home.html",context)

def detail(request,course_id):
	return HttpResponse("you are viewing " + course_id )

def add_course(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			new_course = form.save()
			return HttpResponseRedirect(reverse('sys_main:sysmain'))

	else :
		form = CourseForm()

	return render(request, "sys_main/add_course.html", {'form' : form})
