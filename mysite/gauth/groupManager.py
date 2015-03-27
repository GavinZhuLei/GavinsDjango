# -*- coding:utf-8 -*-
# __author__ = '磊'
from django.db.models import Q
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

    def add(self, group):
        """
        添加用户组
        :return:
        """
        if type(group) is not Group:
            return False
        if Group.objects.filter(Q(name=group.name)).count() > 0:
            return False
        group.save()
        return True

    def update(self, group):
        """
        更新用户组
        :param group:
        :return:
        """
        if type(group) is not Group:
            return False
        try:
            oldgroup = Group.objects.get(pk = group.id)
        except:
            return False
        else:
            group.save()
            return True

    def set_available(self, id, is_available):
        """
        设置用户组的状态
        :param is_available:
        :return:
        """
        try:
            group = Group.objects.get(pk = id)
        except:
            return False
        else:
            group.is_available = is_available
            group.save()
            return True

    def get_users(self, grouppk):
        """
        获取用户组下面的所有用户
        :param grouppk:
        :return:
        """
        try:
            group = Group.objects.get(pk=grouppk)
        except:
            return None
        else:
            return group.users