from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sysmain/$', views.sysmain, name='sysmain'),
	url(r'^addCourse/$',views.add_course, name='addCourse'),
	url(r'^(?P<course_id>[0-9]+)/add_deadline/(?P<assignment_type>[a-z]+)/$',views.add_deadline, name='add_deadline'),
	url(r'^register/(?P<courseId>[0-9]+)/$',views.register,name='register'),
	url(r'^feedback/(?P<course_id>[0-9]+)/$',views.feedback,name='feedback'),
	url(r'^action_feed/(?P<feedback_id>[0-9]+)/$',views.action_feed,name='action_feed'),
	url(r'^add_oquestion/(?P<feedback_id>[0-9]+)/$', views.add_oquestion, name='add_oquestion'),
	url(r'^feedback/end/(?P<feedback_id>[0-9]+)/$',views.feedbackend,name='feedbackend'),
	url(r'^complete/(?P<feedback_id>[0-9]+)/$',views.complete,name='complete'),
]

