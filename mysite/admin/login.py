# -*- coding: utf-8 -*-
#__author__ = 'Gavin'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse


def login(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/admin/index/')
        # return HttpResponse('ok')
    else:
        return render_to_response('admin/login/index.html',{})
