# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gauth import menu_manager
from gauth.common import MyJSONEncoder
from django.forms.models import model_to_dict


def index(request):
    menus = menu_manager.get_all()
    for menu in menus:

        menu.__dict__['groups'] = [group.name for group in menu.group_set.all()]
    return render_to_response('admin/menu/index.html', {'menus': menus})


def test(request):
    menus = menu_manager.get_all()
    for menu in menus:

        menu.__dict__['groups'] = [group.name for group in menu.group_set.all()]
    res = [model_to_dict(menu) for menu in menus]
    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))