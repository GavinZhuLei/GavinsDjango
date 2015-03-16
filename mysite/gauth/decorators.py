# -*- coding:utf-8 -*-
# __author__ = '磊'
"""
装饰器：实现用于身份验证的aop
"""
from django.http import HttpResponse
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(request):

        if request.user.is_authenticated():
            return func(request)
        else:
            return HttpResponse('认证失败')
    return wrapper