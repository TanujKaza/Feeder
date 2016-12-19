from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from main.models import Course,Assignment
from main.forms import AssignmentForm
from django.utils.datetime_safe import datetime

@login_required(login_url="/login/")
def home(request):
	current_user = request.user
	prof_id = current_user.id
	courses = Course.objects.filter(instructor = prof_id)
	context = {"courses" : courses}
	return render(request,"main/home.html",context)

def view_ass(request,course_id):
	assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
	assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
	context = {"assignments" : assignments,"assignments_c" : assignments_c}
	return render(request,"main/assignments.html",context)

def edit_ass(request,assignment_id):
	assignment = Assignment.objects.filter(id = assignment_id)
	form = AssignmentForm(initial = {'ass_name': assignment[0].ass_name, 'ass_text': assignment[0].ass_text, 'ass_deadline' : assignment[0].ass_deadline})

	return render(request, "main/edit_assignment.html", {'form' : form, 'assignment_id' : assignment_id})

def save_ass(request,assignment_id):
	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			assignment = Assignment.objects.filter(id = assignment_id)[0]
			assignment.ass_name = request.POST.get('ass_name')
			assignment.ass_text = request.POST.get('ass_text')
			date = request.POST.get('ass_deadline')
			if date[2] == "/":
				month = date[0:2]
				day = date[3:5]
				year = date[6:]
				assignment.ass_deadline = year + "-" + month + "-" + day
			else:
				assignment.ass_deadline = date
			assignment.save()

			course_id = assignment.course_id
			assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
			assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
			context = {"assignments" : assignments,"assignments_c" : assignments_c}

	else:
		assignments = Assignment.objects.filter(id = assignment_id)
		course_id = assignments[0].course_id
		assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
		assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
		context = {"assignments" : assignments,"assignments_c" : assignments_c}

	return render(request,"main/assignments.html",context)

def add_ass(request,course_id):
	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			assignment = Assignment()
			assignment.ass_name = request.POST.get('ass_name')
			assignment.ass_text = request.POST.get('ass_text')
			date = request.POST.get('ass_deadline')
			if date[2] == "/":
				month = date[0:2]
				day = date[3:5]
				year = date[6:]
				assignment.ass_deadline = year + "-" + month + "-" + day
			else:
				assignment.ass_deadline = date
			assignment.course_id = course_id

			assignment.save()
			current_user = request.user
			prof_id = current_user.id
			courses = Course.objects.filter(instructor = prof_id)
			context = {"courses" : courses}
			return render(request,"main/home.html",context)

	else:
		form = AssignmentForm()
		context = {'form':form,'course_id':course_id}

	return render(request, "main/add_assignment.html",context)

def delete_ass(request,assignment_id):
	assignment = Assignment.objects.filter(id = assignment_id)[0]
	course_id = assignment.course_id

	assignment.delete()

	assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
	assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
	context = {"assignments" : assignments,"assignments_c" : assignments_c}

	return render(request,"main/assignments.html",context)

def cancel_ass(request,course_id):
	current_user = request.user
	prof_id = current_user.id
	courses = Course.objects.filter(instructor = prof_id)
	context = {"courses" : courses}
	return render(request,"main/home.html",context)




	

