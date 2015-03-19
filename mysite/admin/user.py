# -*- coding:utf-8 -*-
# __author__ = '磊'
from django.shortcuts import render_to_response
from gauth.userManager import UserManager
from gauth.common import MyJSONEncoder
from django.http import HttpResponse
import json


def index(request):
    return render_to_response('admin/user/index.html',{})


def edit(request, user_id):
    if user_id != 0:
        usermanager = UserManager()
        user = usermanager.get_bypk(user_id)

        return render_to_response('admin/user/edit.html',{'user_id':user_id,'user':user})

    return render_to_response('admin/user/edit.html',{'user_id':user_id})


def update(request):
    return render_to_response('admin/user/edit.html',{})


def users_data(request):
    usermanager = UserManager()
    users = usermanager.get_all
    draw = request.POST['draw']
    res= _load_data(users,draw)

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def _load_data(users, draw):
    res = {}
    res['draw'] = draw
    res['data'] = []
    res['recordsFiltered'],res['recordsTotal'] = len(users),len(users)
    for user in users:
        row = []
        row.append('<input type="checkbox" name="id[]" value="'+str(user.pk)+'">')
        row.append('1')
        row.append(user.username)
        row.append(user.password)
        row.append(user.nickname)
        row.append(user.email)
        row.append(user.phone)
        row.append(user.create_time)
        row.append(user.last_login_time)
        row.append('<span class="label label-sm label-success">正常</span>')
        row.append('<a href="javascript:;" data-id="'+str(user.pk)+'" class="btn btn-xs default btn-editable"><i class="fa fa-pencil"></i> 编辑</a>')

        res['data'].append(row)

    return res