from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from main.models import *
from main.forms import AssignmentForm
from django.utils.datetime_safe import datetime
import main.mycharts as mycharts
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/login/")
def home(request):
	current_user = request.user
	prof_id = current_user.id
	courses = Course.objects.filter(instructor = current_user)
	context = {"courses" : courses}
	return render(request,"main/home.html",context)

@login_required(login_url="/login/")
def view_ass(request,course_id):
	assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
	assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
	context = {"assignments" : assignments,"assignments_c" : assignments_c}
	return render(request,"main/assignments.html",context)

@login_required(login_url="/login/")
def edit_ass(request,assignment_id):
	assignment = Assignment.objects.filter(id = assignment_id)
	form = AssignmentForm(initial = {'ass_name': assignment[0].ass_name, 'ass_text': assignment[0].ass_text, 'ass_deadline' : assignment[0].ass_deadline})

	return render(request, "main/edit_assignment.html", {'form' : form, 'assignment_id' : assignment_id})

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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
			courses = Course.objects.filter(instructor = current_user)
			context = {"courses" : courses}
			return render(request,"main/home.html",context)

	else:
		form = AssignmentForm()
		context = {'form':form,'course_id':course_id}

	return render(request, "main/add_assignment.html",context)

@login_required(login_url="/login/")
def delete_ass(request,assignment_id):
	assignment = Assignment.objects.filter(id = assignment_id)[0]
	course_id = assignment.course_id

	assignment.delete()

	assignments = Assignment.objects.filter(course = course_id,	ass_deadline__gte = datetime.now())
	assignments_c = Assignment.objects.filter(course = course_id,	ass_deadline__lt = datetime.now())
	context = {"assignments" : assignments,"assignments_c" : assignments_c}

	return render(request,"main/assignments.html",context)

@login_required(login_url="/login/")
def cancel_ass(request,course_id):
	current_user = request.user
	prof_id = current_user.id
	courses = Course.objects.filter(instructor = current_user)
	context = {"courses" : courses}
	return render(request,"main/home.html",context)

@login_required(login_url="/login/")
def view_feed(request,course_id):
	feedback = Feedback_f.objects.filter(course = course_id,	form_deadline__gte = datetime.now())
	feedback_c = Feedback_f.objects.filter(course = course_id,	form_deadline__lt = datetime.now())
	context = {"feedback" : feedback,"feedback_c" : feedback_c}
	return render(request,"main/view_feedback.html",context)

@login_required(login_url="/login/")
def view_ques(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	course_id = feedback.course_id
	feedback_o = feedback.feedback_o_set.all()
	feedback_s = feedback.feedback_s_set.all()

	context = {'feedback':feedback,'course_id':course_id,'feedback_id':feedback_id,'feedback_o':feedback_o,'feedback_s':feedback_s}

	return render(request,"main/questions.html",context)

@login_required(login_url="/login/")
def add_feed(request,course_id):
	feedback_m = Feedback_f()
	feedback_m.course_id = course_id

	feedback_m.save()

	feedback_id = feedback_m.id

	feedback_e = feedback_m.feedback_o_set.all()
	feedback_n = Feedback_o.objects.all()
	feedback_n = feedback_n.exclude(feed = feedback_m)

	feedback_es = feedback_m.feedback_s_set.all()
	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback_m)
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es}

	return render(request,"main/add_feedback.html",context)

@login_required(login_url="/login/")
def activity_feed(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	if request.method == 'POST':
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
	feedback_n = feedback_n.exclude(feed = feedback)

	feedback_es = feedback.feedback_s_set.all()
	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback)
	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es}

	return render(request,"main/add_feedback.html",context)

@login_required(login_url="/login/")
def add_ques(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	if request.method == 'POST':
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
	feedback_n = feedback_n.exclude(feed = feedback)

	feedback_es = feedback.feedback_s_set.all()
	feedback_ns = Feedback_s.objects.all()
	feedback_ns = feedback_ns.exclude(feed = feedback)

	context = {'feedback_id':feedback_id,'feedback':feedback_n,'feedback_e':feedback_e,'feedbacks':feedback_ns,'feedback_es':feedback_es}

	return render(request,"main/add_feedback.html",context)

@login_required(login_url="/login/")
def compl_feed(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	feedback.feed_title = request.POST.get('feed_title')
	feedback.form_deadline = request.POST.get('feed_deadline')
	feedback.save()

	current_user = request.user
	prof_id = current_user.id
	courses = Course.objects.filter(instructor = current_user)
	context = {"courses" : courses}
	return render(request,"main/home.html",context)

@login_required(login_url="/login/")
def view_results(request,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	feedback_o = Feedback_o.objects.filter(feed = feedback)

	objective_dict = {}
	for feed_iter in feedback_o:
		feedback_ao = Feedback_ao.objects.filter(form = feedback,feed = feed_iter)
		feedback_ao = list(feedback_ao[:1])
		if feedback_ao:
			total_responses = feedback_ao[0].option_1 + feedback_ao[0].option_2 + feedback_ao[0].option_3 + feedback_ao[0].option_4 + feedback_ao[0].option_5
			feedback_ao = feedback_ao[0]
		else:
			total_responses = None
			feedback_ao = None
		temp_dict = {}
		temp_dict[feedback_ao] = total_responses
		objective_dict[feed_iter] = temp_dict

	feedback_s = Feedback_s.objects.filter(feed = feedback)
	course_id = feedback.course_id

	context = {'course_id':course_id,'feedback_id':feedback_id,'feedback_o':objective_dict,'feedback_s':feedback_s}

	return render(request,"main/results.html",context)

@login_required(login_url="/login/")
def view_graph(request,feedback_id):
	feedback = Feedback_ao.objects.get(id = feedback_id)
	
	d = mycharts.MyLineChartDrawing()    

	d.height = 300
	d.chart.height = 300


	d.width = 600
	d.chart.width = 500

	d.title._text = "Line Chart"



	d.XLabel._text = "Ratings"
	d.YLabel._text = "Number of Responses"

	d.chart.data = [((1,feedback.option_1), (2,feedback.option_2), (3,feedback.option_3), (4,feedback.option_4), (5,feedback.option_5)),]



	labels =  ["Label One","Label Two"]
	if labels:
	    # set colors in the legend
	    d.Legend.colorNamePairs = []
	    for cnt,label in enumerate(labels):
	            d.Legend.colorNamePairs.append((d.chart.lines[cnt].strokeColor,label))

	#get a GIF (or PNG, JPG, or whatever)
	binaryStuff = d.asString('jpg')
	context = {'binarystuff':binaryStuff,'image':'image/jpg'}
	return HttpResponse(binaryStuff, 'image/jpg')

@login_required(login_url="/login/")
def view_answers(request,question_id,feedback_id):
	feedback = Feedback_f.objects.get(id = feedback_id)
	feedback_q = Feedback_s.objects.get(id = question_id)
	feedback_a = Feedback_a.objects.filter(question=feedback_q,form=feedback)
	course_id = feedback.course_id
	feedback_id = feedback.id

	context = {'feedback_id':feedback_id,'course_id':course_id,'feedback_q':feedback_q,'feedback_a':feedback_a,'feedback':feedback}
	return render(request,"main/subjective_results.html",context)

@csrf_exempt
def view_fandroid(request):
	if request.method == 'POST':
		feedback_id = request.POST.get('feedback_id')
		feedback = Feedback_f.objects.get(id = feedback_id)
		feedback_qa = Feedback_o.objects.get(feed = feedback)
		feedback_qs = Feedback_s.objects.get(feed = feedback)

		feedback_final = []
		feedback_final.append(feedback_qa)
		feedback_final.append(feedback_qs)
		# print(feedback_final)

		return json.dumps(feedback_final)
	else:
		feedback_final = ["Default"]
		return json.dumps(feedback_final)





    









	


