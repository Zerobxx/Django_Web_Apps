from django.contrib import admin
from EventLog import models
from django import forms
from django.contrib.auth.models import Permission
# Register your models here.

class HardwareEventAdmin(admin.ModelAdmin):
    list_display = ('malfunction_date', 'colored_event_level', 'hostname', 'manufacturer', 'malfunction_part', 'part_model', 'reason_judge', 'restore_time')
    search_fields = ('hostname',)
    list_filter = ('event_level', 'malfunction_date', 'manufacturer', 'malfunction_part')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'model', 'target_device', 'parameters', 'num', 'storage_place')
    search_fields = ('name', 'model')
    list_filter = ('name', 'distributor', 'model', 'storage_place')

class Test_DeviceAdmin(admin.ModelAdmin):
    list_display = ('location', 'name', 'model', 'manufacturer', 'num', 'arrivaldate', 'test_engineer', 'purpose', 'result', 'colored_if_give_back')
    search_fields = ('name', 'manufacturer', 'model')
    list_filter = ('location', 'manufacturer', 'if_give_back')

admin.site.register(models.Hardware_Event, HardwareEventAdmin)
admin.site.register(models.IDC)
# admin.site.register(models.EventLog)
admin.site.register(models.UserProfile)
admin.site.register(models.Inventory, InventoryAdmin)
admin.site.register(models.Test_Device, Test_DeviceAdmin)


