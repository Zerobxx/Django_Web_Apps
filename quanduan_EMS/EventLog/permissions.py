from django.shortcuts import render
import functools

def perm_check(request, *args, **kwargs):


def check_permission(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):
            return func(request, *args, **kwargs)
        return render(request, '403.html')
    return wrapper

