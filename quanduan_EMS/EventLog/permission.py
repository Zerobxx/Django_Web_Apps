#coding=utf-8

from django.shortcuts import render
from EventLog import models
from django.db.models import Q
from django.core.urlresolvers import resolve
import functools

def perm_check(request, *args, **kwargs):
    url_obj = resolve(request.path_info)
    url_name = url_obj.url_name
    perm_name = ''
    if url_name:
        url_method, url_args = request.method, request.GET
        url_args_list = []
        for i in url_args:
            url_args_list = url_args_list.append(str(url_args[i]))
        url_args_list = ','.join(url_args_list)
        get_perm = models.Permission.objects.filter(Q(urlname= url_name) and Q(perm_method= url_method) and Q(argument_list = url_args_list))
        if get_perm:
            for i  in get_perm:
                perm_name = i.codename
                perm_str = 'EventLog.%s' % perm_name
                if request.user.has_perm(perm_str):
                    print(u'===权限已匹配===')
                    return True
                else:
                    print(u'===权限没有匹配===')
                    return False
        else:
            return False

def check_permission(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):
            return func(request, *args, **kwargs)
        return render(request, '403.html')
    return wrapper