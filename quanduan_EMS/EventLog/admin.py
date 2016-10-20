from django.contrib import admin
from EventLog import models
from django import forms
# Register your models here.

class HardwareEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'colored_event_level', 'malfunction_date', 'hostname', 'manufacturer', 'malfunction_part','reason_judge')
    search_fields = ('hostname',)
    list_filter = ('event_level', 'malfunction_date', 'manufacturer', 'malfunction_part')

admin.site.register(models.Hardware_Event, HardwareEventAdmin)
admin.site.register(models.IDC)
# admin.site.register(models.EventLog)
