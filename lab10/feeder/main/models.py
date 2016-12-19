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
	instructor = models.ForeignKey(User,default=2)

	def __str__(self):
		return self.course_name

class Student(models.Model):
	roll_number = models.IntegerField(default=0)
	email_id = models.EmailField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
	ass_name = models.CharField(max_length=200)
	ass_text = models.TextField()
	ass_deadline = models.DateTimeField()
	ass_published = models.DateTimeField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Feedback_f(models.Model):
	feed_title = models.CharField(max_length=200)
	feed_deadline = models.DateTimeField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Feedback_s(models.Model):
	question_text = models.TextField()
	feed = models.ForeignKey(Feedback_f, on_delete=models.CASCADE)

class Feedback_o(models.Model):
	question_text = models.TextField()
	option_1 = models.IntegerField(default=0)
	option_2 = models.IntegerField(default=0)
	option_3 = models.IntegerField(default=0)
	option_4 = models.IntegerField(default=0)
	option_5 = models.IntegerField(default=0)
	feed = models.ForeignKey(Feedback_f, on_delete=models.CASCADE)

class Feedback_a(models.Model):
	answer_text = models.TextField()
	student_roll = models.IntegerField(default=0)
	question = models.ForeignKey(Feedback_s, on_delete=models.CASCADE)