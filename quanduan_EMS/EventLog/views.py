from django.shortcuts import render
from EventLog import models
from EventLog.permission import check_permission
# Create your views here.

@check_permission
def list_hardware_event(request):
    hardware_event_list = models.Hardware_Event.objects.all()
    return render(request, 'Hardware_Event_list.html', locals())
