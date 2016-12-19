from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sysmain/$', views.sysmain, name='sysmain'),
]