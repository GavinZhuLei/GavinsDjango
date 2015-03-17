# -*- coding: utf-8 -*-
# __author__ = '磊'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from gauth.userManager import UserManager
from gauth.permissionManager import PermissionManager
from gauth.models import User
from gauth.decorators import login_required
import datetime
import gauth
from django.contrib.auth import decorators


def get_username():
    return {'username': 'zhulei'}


def myprocessor(request):
    get_username()


def index(request):

    # 加载菜单

    return render_to_response('admin/home/layout.html', {},
                              context_instance = RequestContext(request))


def ajax_page(request):
    return render_to_response('admin/test/ajax.html',{})