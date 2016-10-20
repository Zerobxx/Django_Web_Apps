#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IDC(models.Model):
    name = models.CharField(u'IDC机房名称', max_length=128, unique=True)
    addr = models.CharField(u'IDC地址', max_length=128, null=True, blank=True)
    memo = models.TextField(u'备注', blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'IDC机房'
        verbose_name_plural = 'IDC机房'


# class EventLog(models.Model):
#     name = models.CharField(u'事件名称', max_length=128)
#     event_type_choices = (
#         ('IDC_event', u'IDC事件'),
#         ('Network_event', u'网络事件'),
#         ('Hardware_event', u'硬件事件'),
#         ('Other_event', u'其他事件'),
#     )
#     event_type = models.CharField(u'事件类型', max_length=64, choices= event_type_choices)
#     statistics_tag = models.CharField(u'统计标签', max_length=128)
#     detail = models.TextField(u'事件详情')
#     start_time = models.DateTimeField(u'事件发生时间', auto_now_add=True)
#     end_time = models.DateTimeField(u'事件结束时间', blank=True, auto_now=True)
#     memo = models.TextField(u'备注', blank=True, null=True)
#
#     def __unicode__(self):
#         return u'%s___事件源: %s___时间: %s' %(self.name, self.statistics_tag, self.start_time)
#     class Meta:
#         verbose_name = '事件记录'
#         verbose_name_plural = '事件记录'


class Hardware_Event(models.Model):
    malfunction_date = models.DateField(u'故障日期', blank=True, null=True)
    hostname = models.CharField(u'主机名', max_length=64, blank=True, null=True)
    manufacturer_choices = (
        ('kxtech', u'凯翔'),
        ('GIGABYTE', u'技嘉'),
        ('ASUS', u'华硕'),
        ('H3C', u'华三'),
        ('other', u'其他'),
    )
    manufacturer = models.CharField(u'制造商', choices= manufacturer_choices, max_length=64)
    func_type = models.CharField(u'设备类型', max_length=128, blank=True, null=True)
    model = models.CharField(u'型号', max_length=128, blank=True, null=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    event_phenomenon = models.CharField(u'故障现象', max_length=255, blank=True, null=True)
    reason_judge = models.CharField(u'原因判断', max_length=255, blank=True, null=True)
    event_level_choices = (
        ('average', u'普通'),
        ('high', u'重大'),
        ('disaster', u'灾难'),
        ('other', u'其他'),
    )

    event_level = models.CharField(u'故障级别', choices= event_level_choices, max_length=64, default='average')
    malfunction_part = models.CharField(u'故障部件', max_length=64, blank=True, null=True)
    solution = models.CharField(u'解决方法', max_length=255, blank=True, null=True)
    restore_time = models.DateField(u'解决时间', blank=True, auto_now=True)
    IDC = models.CharField(u'IDC机房', max_length=64, blank=True, null=True)
    batch = models.CharField(u'上线批次', max_length=128, blank=True, null=True)
    distributor = models.CharField(u'供应商', max_length=128, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True, null=True)

    class Meta:
        verbose_name = '硬件故障记录'
        verbose_name_plural = '硬件故障记录'

    def colored_event_level(self):
        if self.event_level == 'high':
            cell_html = '<span style="background: orange;">%s</span>'
        elif self.event_level == 'average':
            cell_html = '<span style="background: yellowgreen;">%s</span>'
        elif self.event_level == 'disaster':
            cell_html = '<span style="background: red;">%s</span>'
        else:
            cell_html = '<span >%s</span>'
        return cell_html % self.get_event_level_display()
    colored_event_level.allow_tags = True
    colored_event_level.short_description = u'故障级别'

























