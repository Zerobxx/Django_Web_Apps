from django.shortcuts import render, HttpResponseRedirect
from EventLog import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from EventLog import forms
from EventLog.permissions import check_permission


@check_permission
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


@login_required
def dashboard(request):
    return render(request, 'EventLog/dashbord.html')


@login_required
def hardware_event_detail(request, hareware_event_id):
    hareware_event_obj = models.Hardware_Event.objects.get(id = hareware_event_id)
    if request.method == 'POST':
        form = forms.HardwareEventModelForm(request.POST, instance=hareware_event_obj)
        if form.is_valid():
            form.save()
            base_url = '/'.join(request.path.split('/')[:-2])
            return HttpResponseRedirect(base_url)
    else:
        form = forms.HardwareEventModelForm(instance= hareware_event_obj)
    return render(request, 'EventLog/hardware_event_detail.html', {'hardware_event_form': form})



