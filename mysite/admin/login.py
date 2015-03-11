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

        username = request.POST['username']
        password = request.POST['password']

        usermanager = UserManager()
        auuser = usermanager.authenticate(username,password)
        if auuser is not None:
            gauth.login(request,auuser)
            return HttpResponseRedirect('/admin/index/')
        return HttpResponse('fail')

    else:
        return render_to_response('admin/login/index.html',{},
                                  context_instance = RequestContext(request))
