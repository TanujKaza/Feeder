from django.db import models
from main.choices import *
from django.contrib.auth.models import User

class Course(models.Model):
	course_id = models.CharField(max_length=30, unique = True)
	course_name = models.CharField(max_length=255, unique = True)
	department = models.CharField(choices = DEPARTMENT_CHOICES,max_length=40)
	year = models.IntegerField()
	semester = models.CharField(choices = SEMESTER_CHOICES,max_length=20)
	duration = models.CharField(choices = DURATION_CHOICES,max_length=20)
	instructor = models.ManyToManyField(User)

	def __str__(self):
		return self.course_name

class Student(models.Model):
	roll_number = models.CharField(max_length=20, default=0, unique = True)
	email_id = models.EmailField()
	courses = models.ManyToManyField(Course)
	password = models.CharField(max_length=60, default="")
	
	def __str__(self):
		return "{0}".format(self.roll_number)

class Assignment(models.Model):
	ass_name = models.CharField(max_length=200)
	ass_text = models.TextField(max_length=150,default = '')
	ass_deadline = models.DateTimeField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.ass_name

class Feedback_f(models.Model):
	feed_title = models.CharField(max_length=200)
	form_deadline = models.DateTimeField(blank=True, null=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.feed_title

class Feedback_s(models.Model):
	question_text = models.TextField()
	feed = models.ManyToManyField(Feedback_f)

	def __str__(self):
		return self.question_text

class Feedback_o(models.Model):
	question_text = models.TextField()
	feed = models.ManyToManyField(Feedback_f)

	def __str__(self):
		return self.question_text

class Feedback_ao(models.Model):
	option_1 = models.IntegerField(default=0)
	option_2 = models.IntegerField(default=0)
	option_3 = models.IntegerField(default=0)
	option_4 = models.IntegerField(default=0)
	option_5 = models.IntegerField(default=0)
	feed = models.ForeignKey(Feedback_o,default=1)
	form = models.ForeignKey(Feedback_f,default=1)

class Feedback_a(models.Model):
	answer_text = models.TextField()
	question = models.ForeignKey(Feedback_s, on_delete=models.CASCADE)
	form = models.ForeignKey(Feedback_f,default=1)




