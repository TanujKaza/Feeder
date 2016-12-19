from django.conf.urls import url
import django.contrib.auth.views
from . import views
from login.forms import LoginForm

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register1/(?P<course_id>[a-zA-Z0-9]+)/$', views.register1,name='register1'),
    url(r'^reason/$', views.reason, name='reason'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/login'}),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login/login.html', 'authentication_form': LoginForm}), 
    url(r'^privacy/$', views.privacy, name='privacy'),
    
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^about/$', views.about, name='about'),
	url(r'^authenticate/$', views.authenticate, name='authenticate'),
]
