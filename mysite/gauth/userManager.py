# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
from models import User
from django.db.models import Q
import common


class UserManager():
    def __init__(self):
        pass

    @property
    def get_all(self):
        return User.objects.all()

    def add(self, user):
        # 检查用户名是否存在
        User.objects

        # 对用户密码加密
        user.password = common.md5(user.password)
        user.save()

    def get_one(self, username):
        user = User.objects.get(Q(username=username))
        return user
