from main.models import Course, Assignment
from django import forms
from main.choices import *

class JQueryUIDatepickerWidget(forms.DateInput):
	def __init__(self, **kwargs):
		super(forms.DateInput, self).__init__(attrs={"size":50, "class": "dateinput", "name":"assignment_deadline"}, **kwargs)

	class Media:
		css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
		js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)

class CourseForm(forms.ModelForm):
	course_id = forms.CharField(label="Course Code", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
	course_name = forms.CharField(label="Course Name", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	department = forms.ChoiceField(choices = DEPARTMENT_CHOICES,label="Department",widget=forms.Select(attrs={'class': 'form-control'}))
	year = forms.CharField(label="Year", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
	semester = forms.ChoiceField(choices = SEMESTER_CHOICES,label="Semester",widget=forms.Select(attrs={'class': 'form-control'}))
	duration = forms.ChoiceField(choices = DURATION_CHOICES,label="Duration",widget=forms.Select(attrs={'class': 'form-control'}))
	instructor = forms.MultipleChoiceField(choices = INSTRUCTOR_CHOICES,label="Instructor",widget=forms.SelectMultiple(attrs={'class':'form-control'}))


	class Meta:
		model = Course
		fields = ['course_id','course_name','department','year','semester','duration']

class Assignment_form(forms.Form):
	ass_deadline = forms.DateTimeField(label="Assignment Deadline",widget=JQueryUIDatepickerWidget)

	ass_text = forms.CharField(label="Assignment Description", max_length=6000,widget=forms.Textarea(attrs={'class': 'form-control'}))




