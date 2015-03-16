# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
from django import forms


class LoginForm(forms.Form):
    """
    用户登录
    """
    username = forms.CharField()
    password = forms.CharField()
    remember = forms.BooleanField(required=False)