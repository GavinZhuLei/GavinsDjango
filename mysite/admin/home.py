# -*- coding: utf-8 -*-
# __author__ = '磊'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template


def get_username():
    return {'username': 'zhulei'}


def myprocessor(request):
    get_username()


def index(request):
    # c = RequestContext(request,[myprocessor])
    # t = get_template('admin/home/index.html')
    # return HttpResponse(t.render(c))

    return render_to_response('admin/home/index.html', {},
                              context_instance=RequestContext(request, [myprocessor]))