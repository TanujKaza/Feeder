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
	url(r'^view/feedback/(?P<course_id>[0-9]+)/$', views.view_feed, name='view_feed'),
	url(r'^view/questions/(?P<feedback_id>[0-9]+)/$', views.view_ques, name='view_ques'),
	url(r'^add/feedback/(?P<course_id>[0-9]+)/$', views.add_feed, name='add_feed'),
	url(r'^activity/feedback/(?P<feedback_id>[0-9]+)/$', views.activity_feed, name='activity_feed'),
	url(r'^add/question/(?P<feedback_id>[0-9]+)/$', views.add_ques, name='add_ques'),
	url(r'^feedback/complete/(?P<feedback_id>[0-9]+)/$', views.compl_feed, name='compl_feed'),
	url(r'^view/results/(?P<feedback_id>[0-9]+)/$', views.view_results, name='view_results'),
	url(r'^view/graph/(?P<feedback_id>[0-9]+)/$', views.view_graph, name='view_graph'),
	url(r'^view/subjective/(?P<question_id>[0-9]+)/(?P<feedback_id>[0-9]+)/$', views.view_answers, name='view_answers'),
	url(r'^feedback/android/$', views.view_fandroid, name='view_fandroid'),	
]