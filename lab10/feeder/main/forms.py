from main.models import Assignment
from django.forms import ModelForm
from django import forms

class JQueryUIDatepickerWidget(forms.DateInput):
	def __init__(self, **kwargs):
		super(forms.DateInput, self).__init__(attrs={"size":50, "class": "dateinput", "name":"assignment_deadline"}, **kwargs)

	class Media:
		css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
		js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)

class AssignmentForm(forms.Form):
	ass_name = forms.CharField(label="Assignment Name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'assignment_name'}))

	ass_text = forms.CharField(label="Assignment Text", max_length=6000,
                               widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'assignment_text'}))

	ass_deadline = forms.DateField(label="Assignment Deadline",widget=JQueryUIDatepickerWidget)

