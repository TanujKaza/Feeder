from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'', include('main.urls')),
	url(r'', include('login.urls')),
	url(r'', include('sysadmin.urls')),
	url(r'', include('sys_main.urls')),
    url(r'^admin/', admin.site.urls),   
]