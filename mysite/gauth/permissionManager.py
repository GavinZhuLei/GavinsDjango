# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
from gauth.models import Permission


class PermissionManager():
    def __init__(self):
        pass

    def get_all(self):
        return Permission.objects.all()