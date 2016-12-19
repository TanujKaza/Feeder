from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$', views.home, name='home'),
	url(r'^view_ass/(?P<course_id>[0-9]+)/$', views.view_ass, name='view_ass'),
	url(r'^edit_ass/(?P<assignment_id>[0-9]+)/$', views.edit_ass, name='edit_ass'),
	url(r'^save_ass/(?P<assignment_id>[0-9]+)/$', views.save_ass, name='save_ass'),
	url(r'^add_ass/(?P<course_id>[0-9]+)/$', views.add_ass, name='add_ass'),
	url(r'^delete_ass/(?P<assignment_id>[0-9]+)/$', views.delete_ass, name='delete_ass'),
	url(r'^cancel_ass/(?P<course_id>[0-9]+)/$', views.cancel_ass, name='cancel_ass'),
]