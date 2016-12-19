from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,user_passes_test
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
import csv
from .forms import CourseForm, Assignment_form

from django.contrib.auth.models import User
@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def sysmain(request):
	s = Student.objects.all()
	with open('student.csv', 'rt') as studentfile:
		data = csv.DictReader(studentfile)
		for row in data:
			if s:
				student_file = Student.objects.filter(roll_number=row['roll_number'])
				if not student_file:
					student = Student(roll_number=row['roll_number'],email_id=row['email_id'],password=row['password'])
					student.save()
			else :
				student = Student(roll_number=row['roll_number'],email_id=row['email_id'],password=row['password'])
				student.save()

	courses = Course.objects.all()
	context = {"courses" : courses}
	return render(request,"sys_main/home.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def add_course(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			course = Course()
			course.course_id = request.POST.get('course_id')
			course.course_name = request.POST.get('course_name')
			course.department = request.POST.get('department')
			course.year = request.POST.get('year')
			course.semester = request.POST.get('semester')
			course.duration = request.POST.get('duration')
			instructor_ids = request.POST.getlist('instructor')

			for instruct in instructor_ids:
				course.save()
				instructor = User.objects.get(id=instruct)
				instructor.course_set.add(course)
			
			course.save()
			courses = Course.objects.all()
			context = {"courses" : courses}
			return HttpResponseRedirect('/'+ str(course.id)+'/add_deadline/default/')

	else :
		form = CourseForm()

	return render(request, "sys_main/add_course.html", {'form' : form})

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def add_deadline(request,course_id,assignment_type):
	if request.method == 'POST':
		form =  Assignment_form(request.POST)
		if form.is_valid():
			assignment = Assignment()
			assignment.ass_name = assignment_type
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
			form = Assignment_form()
	else:
		form = Assignment_form()

	context = {'form':form,'course_id':course_id}
	return render(request,"sys_main/add_exam.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def register(request,courseId):
	course = Course.objects.get(id=courseId)
	if request.method == 'POST':
		roll_nums = request.POST.getlist('students')
		for i in roll_nums:
			if 'add' in request.POST:
				s = Student.objects.get(roll_number=i)
				course.student_set.add(s)
			elif 'delete' in request.POST:
				s = Student.objects.get(roll_number=i)
				course.student_set.remove(s)
	
	students_e = course.student_set.all()
	students = Student.objects.all()
	students = students.exclude(courses=course)
	return render(request,"sys_main/register.html",{'course' : course, 'students' : students, 'students_e' : students_e})

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def feedback(request,course_id):
	success = False
	feedback_m = Feedback_f()
	feedback_m.feed_title = "Midsem Feedback"
	feedback_m.course_id = course_id

	feedback_m.save()

	feedback_id = feedback_m.id

	feedback_e = feedback_m.feedback_o_set.all()

	feedback_default = Feedback_o.objects.all()[0:4]
	for feed_default in feedback_default:
		feedback_m.feedback_o_set.add(feed_default.id)

	feedback_n = Feedback_o.objects.all()
	feedback_n = feedback_n.exclude(feed = feedback_m)[0:4]

	feedback_es = feedback_m.feedback_s_set.all()

	feedback_default = Feedback_s.objects.all()[0:2]
	for feed_default in feedback_default:
		feedback_m.feedback_s_set.add(feed_default.id)

	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback_m)[0:2]
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es,'success':success}

	return render(request,"sys_main/feedback.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def action_feed(request,feedback_id):
	success = False
	feedback = Feedback_f.objects.get(id = feedback_id)
	if request.method == 'POST':
		success = (not (request.POST.get('form_type') == "False"))
		feedback_ids = request.POST.getlist('feedback')
		for i in feedback_ids:
			if 'add' in request.POST:
				if request.POST.get('question_type') == "objective":
					f = Feedback_o.objects.get(id=i)
					feedback.feedback_o_set.add(f)
				else:
					f = Feedback_s.objects.get(id=i)
					feedback.feedback_s_set.add(f)

			elif 'delete' in request.POST:
				if request.POST.get('question_type') == "objective":
					f = Feedback_o.objects.get(id=i)
					feedback.feedback_o_set.remove(f)
				else:
					f = Feedback_s.objects.get(id=i)
					feedback.feedback_s_set.remove(f)

	feedback_e = feedback.feedback_o_set.all()
	feedback_n = Feedback_o.objects.all()
	feedback_n = feedback_n.exclude(feed = feedback)[0:4]

	feedback_es = feedback.feedback_s_set.all()
	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback)[0:2]
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es,'success':success}

	return render(request,"sys_main/feedback.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def add_oquestion(request,feedback_id):
	success = False
	feedback = Feedback_f.objects.get(id = feedback_id)
	if request.method == 'POST':
		success = (not (request.POST.get('form_type') == "False"))
		feedback_id = request.POST.get('feedback_id')
		if request.POST.get('feedback_type') == "objective":
			feedback_new = Feedback_o()
			feedback_new.question_text = request.POST.get('question_text')
			if feedback_new.question_text:
				feedback_new.save()
				feedback.feedback_o_set.add(feedback_new)
		else:
			feedback_new = Feedback_s()
			feedback_new.question_text = request.POST.get('question_text')
			if feedback_new.question_text:
				feedback_new.save()
				feedback.feedback_s_set.add(feedback_new)

	feedback_e = feedback.feedback_o_set.all()
	feedback_n = Feedback_o.objects.all()
	feedback_n = feedback_n.exclude(feed = feedback)[0:4]

	feedback_es = feedback.feedback_s_set.all()
	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback)[0:2]
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es,'success':success}

	return render(request,"sys_main/feedback.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def feedbackend(request,feedback_id):
	success = True
	feedback = Feedback_f.objects.get(id = feedback_id)
	feedback.form_deadline = request.POST.get('feed_deadline')
	feedback.save()

	course_id = feedback.course_id

	feedback_m = Feedback_f()
	feedback_m.feed_title = "Endsem Feedback"
	feedback_m.course_id = course_id

	feedback_m.save()

	feedback_id = feedback_m.id

	feedback_e = feedback_m.feedback_o_set.all()

	feedback_default = Feedback_o.objects.all()[0:4]
	for feed_default in feedback_default:
		feedback_m.feedback_o_set.add(feed_default.id)

	feedback_n = Feedback_o.objects.all()
	feedback_n = feedback_n.exclude(feed = feedback_m)[0:4]

	feedback_es = feedback_m.feedback_s_set.all()

	feedback_default = Feedback_s.objects.all()[0:2]
	for feed_default in feedback_default:
		feedback_m.feedback_s_set.add(feed_default.id)

	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback_m)[0:2]
	
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es,'success':success}

	return render(request,"sys_main/feedback.html",context)

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def complete(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	feedback.form_deadline = request.POST.get('feed_deadline')
	feedback.save()
	course_id = feedback.course_id

	course = Course.objects.get(id = course_id)
	context = {"course" : course}
	return render(request,"sys_main/complete.html",context)




