# -*- coding:utf-8 -*-
# __author__ = 'Gavin'

"""
中间件 ； 处理封装request请求
"""
from django.utils.functional import SimpleLazyObject
import gauth


class AuthenticationMiddleware(object):
    def process_request(self, request):
        user = gauth.get_user(request)
        # request.user = SimpleLazyObject(user)
        request.user = user
