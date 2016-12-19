from django.conf.urls import url
import django.contrib.auth.views
from login.forms import LoginForm

urlpatterns = [
    url(r'^sysadmin/$', django.contrib.auth.views.login, {'template_name': 'sysadmin/sysadmin.html', 'authentication_form': LoginForm}),
    url(r'^syslogout/$', django.contrib.auth.views.logout, {'next_page': '/sysadmin'}),
]