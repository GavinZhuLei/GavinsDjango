# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
from models import User
from django.db.models import Q
import common

class UserManager(object):
    def __init__(self):
        pass

    @property
    def get_all(self):
        return User.objects.all()

    def get(self, start, length):
        """
        分页获取用户数据
        :param start:开始位置
        :param length:获取数据条数
        :return:
        """
        return User.objects.all()[start : (start + length)]

    def get_count(self):
        return User.objects.count()

    def add(self, user):
        # 检查用户名是否存在
        if User.objects.filter(Q(username=user.username)).count() > 0:
            return False

        # 对用户密码加密
        user.password = common.md5(user.password)
        user.save()
        return True

    def update(self, user):
        try:
            olduser = User.objects.get(pk=user.id)
        except:
            return False
        else:
            user.password = olduser.password
            user.save()
            return True

    def update_is_active(self, pk, is_active):
        """
        更新用户状态
        :param pk:
        :param is_active:
        :return:
        """
        try:
            user = User.objects.get(pk = pk)
        except:
            return False
        else:
            user.is_active = is_active
            user.save()
            return True

    def get_one(self, username):
        try:
            user = User.objects.get(Q(username=username))
            return user
        except:
            return None

    def get_bypk(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except:
            return None

    def authenticate(self, username, password):
        """
        认证用户名密码是否正确
        :param username:
        :param password:
        :return:
        """
        user = self.get_one(username)
        if user is not None:
            if common.md5(password) == user.password:
                return user
        return None
