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
    # c = RequestContext(request,[myprocessor])
    # t = get_template('admin/home/index.html')
    # return HttpResponse(t.render(c))

    # return render_to_response('admin/home/index.html', {},
    #                           context_instance=RequestContext(request, [myprocessor]))

    # 加载菜单

    return render_to_response('admin/home/layout.html', {},
                              context_instance = RequestContext(request))


@login_required
def test(request):
    usermanager = UserManager()

    users = usermanager.get_all
    # users = User.objects.all()

    permissionmanager = PermissionManager()
    actions = permissionmanager.get_all()
    
    return render_to_response('admin/home/test.html', {'users': users,'actions':actions})


def test1(request):
    usermanager = UserManager()
    user = User()
    user.password = '123456'
    user.create_time = datetime.datetime.now()
    user.last_login_time = datetime.datetime.now()
    user.username = 'zhulei'
    if usermanager.add(user):
        return HttpResponse('success')
    return HttpResponse('fail')

def test2(request):
    usermanager = UserManager()
    user = usermanager.get_one('zhulei')

    return render_to_response('admin/home/test2.html',{'user':user})