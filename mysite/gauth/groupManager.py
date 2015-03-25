# -*- coding:utf-8 -*-
# __author__ = '磊'
from gauth.models import Group


class GroupManager(object):
    """
    用户组管理
    """
    def __int__(self):
        pass

    def get(self, start, length):
        """
        分页获取用户组信息
        :param start:
        :param length:
        :return:
        """
        return Group.objects.all()[start : (start + length)]

    def get_count(self):
        """
        获取用户组总的条数
        :return:
        """
        return Group.objects.count()