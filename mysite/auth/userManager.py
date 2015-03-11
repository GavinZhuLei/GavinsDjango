# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
from models import User
import common


class UserManager():
    def __init__(self):
        pass

    @property
    def get_all(self):
        return User.objects.all()

    def add(self, user):
        # 对用户密码加密
        user.password = common.md5(user.password)
        user.save()
