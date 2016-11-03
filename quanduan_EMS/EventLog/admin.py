from django.contrib import admin
from EventLog import models
from django import forms
from django.contrib.auth.models import Permission
# Register your models here.

class HardwareEventAdmin(admin.ModelAdmin):
    list_display = ('malfunction_date', 'colored_event_level', 'hostname', 'manufacturer', 'malfunction_part', 'part_model', 'reason_judge', 'restore_time')
    search_fields = ('hostname',)
    list_filter = ('event_level', 'malfunction_date', 'manufacturer', 'malfunction_part')

admin.site.register(models.Hardware_Event, HardwareEventAdmin)
admin.site.register(models.IDC)
# admin.site.register(models.EventLog)
admin.site.register(models.UserProfile)


