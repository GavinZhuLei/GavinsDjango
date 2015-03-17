# -*- coding: utf-8 -*-
#__author__ = 'Gavin'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from gauth.userManager import UserManager
import gauth


def login(request):
    if request.method == 'POST':
        # return HttpResponseRedirect('/admin/index/')

        # username = request.POST['username']
        # password = request.POST['password']
        from forms import LoginForm
        loginf = LoginForm(request.POST)

        if loginf.is_valid():
            usermanager = UserManager()
            username = loginf.cleaned_data['username']
            password = loginf.cleaned_data['password']
            remember = loginf.cleaned_data['remember']
            auuser = usermanager.authenticate(username,password)
            if auuser is not None:
                gauth.login(request,auuser)
                return HttpResponseRedirect('/admin/index/')
        return HttpResponse('fail')

    else:
        return render_to_response('admin/login/index.html',{},
                                  context_instance = RequestContext(request))


def register(request):
    from forms import RegisterForm
    registerf = RegisterForm(request.POST)

    if registerf.is_valid() and registerf.cleaned_data['password'] == registerf.cleaned_data['repassword']:
        from gauth.models import User
        newuser = User()
        newuser.username = registerf.cleaned_data['username']
        newuser.email = registerf.cleaned_data['email']
        newuser.phone = registerf.cleaned_data['phone']
        newuser.password = registerf.cleaned_data['password']

        usermanager = UserManager()
        if usermanager.add(newuser):
            return HttpResponse('success')

    return HttpResponse('fail')


def logout(request):
    gauth.logout(request)
    return HttpResponseRedirect('/admin/login/')

def test(request):
    from forms import LoginForm
    f = LoginForm()
    return HttpResponse(f)