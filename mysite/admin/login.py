# -*- coding: utf-8 -*-
#__author__ = 'Gavin'
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('admin/login/index.html',{})


def login(request):
    return render_to_response('admin/login/login_success.html',{})

def test(request):
    return render_to_response('admin/test/test.html',{})