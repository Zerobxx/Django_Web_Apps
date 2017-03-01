#coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class IDC(models.Model):
    name = models.CharField(u'IDC机房名称', max_length=128, unique=True)
    addr = models.CharField(u'IDC地址', max_length=128, null=True, blank=True)
    # test_field = models.CharField(u'测试字段', max_length=128, null=True)
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
    addr = models.GenericIPAddressField(u'IP', blank=True, null=True)
    # management_IP = models.GenericIPAddressField(u'管理IP', blank=True, null=True)
    manufacturer_choices = (
        ('kxtech', u'凯翔'),
        ('GIGABYTE', u'技嘉'),
        ('ASUS', u'华硕'),
        ('H3C', u'华三'),
        ('Inspur', u'浪潮'),
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
    malfunction_part = models.CharField(verbose_name=u'故障部件', max_length=64, blank=True, null=True)
    part_model = models.CharField(u'部件型号', max_length=64, blank=True,null=True)
    solution = models.CharField(u'解决方法', max_length=255, blank=True, null=True)
    restore_time = models.DateField(u'解决时间', blank=True, null=True)
    IDC = models.CharField(u'IDC机房', max_length=64, blank=True, null=True)
    location = models.CharField(u'位置', max_length=128, blank=True, null=True)
    batch = models.CharField(verbose_name=u'上线批次', max_length=128, blank=True, null=True)
    distributor = models.CharField(verbose_name=u'供应商', max_length=128, blank=True, null=True)
    update_time = models.DateTimeField(u'修改时间', null=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True, null=True)

    class Meta:
        verbose_name = '硬件故障记录'
        verbose_name_plural = '硬件故障记录'
        permissions = (
            ('view_Hardware_Event_list', u'查看硬件事件信息列表'),
        )

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


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名', max_length=64)
    department = models.CharField(u'部门', max_length=64, blank=True, null=True)
    memo = models.CharField(verbose_name=u'备注', max_length=128, blank=True, null=True)
    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'
    def __unicode__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(u'资产名称', max_length=128)

    usage_choices = (
        ('spare_parts', u'备品备件'),
        ('upgrade_parts', u'升级部件'),
        ('remaining_parts', u'剩余部件/用料'),
        ('others', u'其他'),
    )
    usage = models.CharField(u'用途', choices= usage_choices, max_length=64, default='spare_parts')

    importance_level_choices = (
        ('very_important', u'非常重要'),
        ('important', u'重要'),
        ('normal', u'一般'),
        ('unworthy', u'不重要的/无价值的'),
    )
    importance_level = models.CharField(u'重要性（价值）', choices= importance_level_choices, max_length=64, default='normal')

    distributor = models.CharField(u'供应商', max_length=64, blank=True, null=True)
    manufacturer = models.CharField(u'制造商', max_length=64, blank=True, null=True)
    model = models.CharField(u'型号', max_length=128, blank=True, null=True)
    target_device = models.CharField(u'主要适配机型', max_length=128, blank=True, null=True)
    parameters = models.CharField(u'详细参数', max_length=255, blank=True, null=True)
    SN = models.TextField(u'序列号', blank=True, null=True)
    arrivaldate = models.DateField(u'到货日期', blank=True, null=True)
    num = models.IntegerField(u'数量')
    storage_place = models.CharField(u'存放地点', max_length=255, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '库存一览表'
        verbose_name_plural = '库存一览表'

    def colored_importance_level(self):
        if self.importance_level == 'very_important':
            cell_html = '<span style="background: red;">%s</span>'
        elif self.importance_level == 'important':
            cell_html = '<span style="background: orange;">%s</span>'
        elif self.importance_level == 'normal':
            cell_html = '<span style="background: yellowgreen;">%s</span>'
        elif self.importance_level == 'unworthy':
            cell_html = '<span style="background: whitesmoke;">%s</span>'
        else:
            cell_html = '<span >%s</span>'
        return cell_html % self.get_importance_level_display()
    colored_importance_level.allow_tags = True
    colored_importance_level.short_description = u'重要性（价值）'


class Test_Device(models.Model):
    location = models.CharField(u'测试地点', max_length=64)
    name = models.CharField(u'设备名称', max_length=128, blank=True, null=True)
    model = models.CharField(u'型号', max_length=128, blank=True, null=True)
    manufacturer = models.CharField(u'品牌厂商', max_length=64, blank=True, null=True)
    distributor = models.CharField(u'供应商', max_length=64, blank=True, null=True)
    num = models.IntegerField(u'数量', default=1)
    SN = models.CharField(max_length=128, blank=True, null=True)
    arrivaldate = models.DateField(u'借入日期', blank=True, null=True)
    test_engineer = models.CharField(u'测试工程师', max_length=128, blank=True, null=True)
    purpose = models.CharField(u'测试目的', max_length=255, blank=True, null=True)
    result = models.CharField(u'测试结果', max_length=128, blank=True, null=True)
    if_give_back_choices = (
        (True, u'已归还'),
        (False, u'未归还'),
    )
    if_give_back = models.BooleanField(u'是否归还',choices= if_give_back_choices, default=False)
    give_back_date = models.DateField(u'归还日期', blank=True, null=True)
    give_back_method = models.CharField(u'归还方式', max_length=128, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '借测设备一览表'
        verbose_name_plural = '借测设备一览表'

    def colored_if_give_back(self):
        if self.if_give_back == False:
            cell_html = '<span style="background: orange;">%s</span>'
        elif self.if_give_back == True:
            cell_html = '<span style="background: yellowgreen;">%s</span>'
        else:
            cell_html = '<span style="background: red;">%s</span>'
        return cell_html % self.get_if_give_back_display()
    colored_if_give_back.allow_tags = True
    colored_if_give_back.shrt_description = u'是否归还'


class Constracts(models.Model):
    constract_num = models.CharField(u'合同号', max_length=128, primary_key=True)
    constract_name = models.CharField(u'合同名称', max_length=128)
    constract_date = models.DateField(u'签订时间', blank=True, null=True)
    project_batch = models.SmallIntegerField(u'项目批次', default=1)
    contract_details = models.CharField(u'合同详细', max_length=255)
    contract_first_party = models.CharField(u'合同甲方', max_length=128)
    contract_second_party = models.CharField(u'合同乙方', max_length=128)
    maintenance_level_and_time = models.CharField(u'维保级别&时间', max_length=255, blank=True, null=True)
    maintenance_start_time = models.DateField(u'维保起始时间', blank=True, null=True)
    maintenance_end_time = models.DateField(u'维保结束时间', blank=True, null=True)
    whether_under_guarantee_choices = (
        ('under_guarantee', u'保内'),
        ('no_under_guarantee', u'无维保'),
    )
    whether_under_guarantee = models.CharField(u'是否保内', choices=whether_under_guarantee_choices, max_length=64, default='under_guarantee')
    constract_services = models.CharField(u'合同承诺服务', max_length=255)
    memo = models.TextField(u'备注', blank=True, null=True)
    updatetime = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.constract_name

    class Meta:
        verbose_name = '合同及维保'
        verbose_name_plural = '合同及维保'




class Permissions(models.Model):
    codename = models.CharField(u'权限名称', max_length=128)
    urlname = models.CharField(u'URL名称', max_length=255)
    perm_method_choices = (
        ('GET', 'GET'),
        ('POST', 'POST'),
    )
    perm_method = models.CharField(u'请求方法', choices= perm_method_choices, max_length=64, default='GET')
    arguments_list = models.CharField(u'参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    description = models.CharField(u'描述', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.codename

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = '权限表'





















