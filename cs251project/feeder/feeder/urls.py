from django.conf.urls import include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin

urlpatterns = [
	url(r'', include('main.urls')),
	url(r'', include('login.urls')),
	url(r'', include('sysadmin.urls')),
	url(r'', include('sys_main.urls', namespace="sys_main")),
	url(r'^admin/', admin.site.urls),   
]
