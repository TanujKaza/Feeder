from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Feedback_s)
admin.site.register(Feedback_o)
admin.site.register(Feedback_a)
admin.site.register(Feedback_f)
admin.site.register(Feedback_ao)

