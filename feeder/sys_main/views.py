from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,user_passes_test

@login_required(login_url="/sysadmin/")
@user_passes_test(lambda u: u.is_superuser,login_url='/sysadmin/')
def sysmain(request):
    return render(request,"sys_main/home.html")
