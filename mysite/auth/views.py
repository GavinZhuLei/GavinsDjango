# -*- coding: utf-8 -*-
#__author__ = '磊'
from auth.models import Group,User,Permission

def get_all_user(request):
    u1 = User()