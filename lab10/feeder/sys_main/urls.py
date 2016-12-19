from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sysmain/$', views.sysmain, name='sysmain'),
	url(r'^(?P<course_id>[A-Z]{2}[0-9]{3})/$', views.detail, name='detail'),
	url(r'^addCourse/$',views.add_course, name='addCourse'),
]