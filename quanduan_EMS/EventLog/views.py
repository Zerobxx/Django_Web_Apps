from django.shortcuts import render, HttpResponseRedirect
from EventLog import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from EventLog.permission import check_permission
# Create your views here.

@login_required
def list_hardware_event(request):
    hardware_event_list = models.Hardware_Event.objects.all()
    return render(request, 'EventLog/hardware_event_list.html', locals())

@login_required
def index(request):
    return render(request, 'index.html')

def EMS_login(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_error = 'Wrong username or password!'
            return render(request, 'login.html', {'login_error':login_error})
    return render(request, 'login.html')

def EMS_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    return render(request, 'EventLog/dashbord.html')