from main.models import Course
from django.forms import ModelForm

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = '__all__'