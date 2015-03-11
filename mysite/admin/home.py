# -*- coding: utf-8 -*-
# __author__ = '磊'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from gauth.userManager import UserManager
from gauth.models import User
import datetime
import gauth


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

    pk = gauth.get_userpk(request)
    user = gauth.get_user(request)
    request.user = user
    return render_to_response('admin/home/index.html', {'pk':pk,'user':user},
                              context_instance = RequestContext(request))

def test(request):
    usermanager = UserManager()

    users = usermanager.get_all
    # users = User.objects.all()

    return render_to_response('admin/home/test.html', {'users': users})


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