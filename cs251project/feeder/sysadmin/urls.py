from django.conf.urls import url
import django.contrib.auth.views
from login.forms import LoginForm
from . import views

urlpatterns = [
    url(r'^sysadmin/$', django.contrib.auth.views.login, {'template_name': 'sysadmin/sysadmin.html', 'authentication_form': LoginForm}),
    url(r'^syslogout/$', django.contrib.auth.views.logout, {'next_page': '/sysadmin'}),
    url(r'^admin/privacy/$', views.privacy, name='privacy'),
    url(r'^admin/terms/$', views.terms, name='terms'),
    url(r'^admin/about/$', views.about, name='about'),
    url(r'^admin/reason/$', views.reason, name='reason'),
]