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


class RegisterForm(forms.Form):
    """
    用户注册
    """
    username = forms.CharField()
    password = forms.CharField()
    repassword = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()


class UserForm(forms.Form):
    """
    用户管理--编辑
    """
    id = forms.IntegerField(required=False)
    username = forms.CharField()
    password = forms.CharField(required=False)
    repassword = forms.CharField(required=False)
    nickname = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.CharField()
    is_active = forms.BooleanField(required=False)


class PageForm(forms.Form):
    """
    分页获取数据
    """
    draw = forms.IntegerField()
    length = forms.IntegerField()
    start = forms.IntegerField()


class GroupForm(forms.Form):
    """
    用户组
    """
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    description = forms.CharField(required=False)
