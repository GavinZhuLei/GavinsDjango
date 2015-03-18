# -*- coding: utf-8 -*-
# __author__ = '磊'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
import simplejson
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


def ajax_data(request):
    usermanager = UserManager()
    # users = [{'username':'zhulei'},{'username':'zhangsan'}]
    # users = usermanager.get_all
    import json
    # from django.utils.functional import SimpleLazyObject
    # from django.utils
    res = {}
    res['data'] = [['<input type="checkbox" name="id[]" value="1">',1,'12/09/2013','Jhon Doe','Jhon Doe','450.60$',7,'<span class="label label-sm label-info">Closed</span>','<a href="javascript:;" class="btn btn-xs default"><i class="fa fa-search"></i> View</a>'],
                ['<input type="checkbox" name="id[]" value="1">',1,'12/09/2013','Jhon Doe','Jhon Doe','450.60$',7,'<span class="label label-sm label-info">Closed</span>','<a href="javascript:;" class="btn btn-xs default"><i class="fa fa-search"></i> View</a>']]
    res['draw'] = 1
    res['recordsFiltered'] = 2
    res['recordsTotal'] = 2

    from gauth.common import MyJSONEncoder

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))
