# -*- coding:utf-8 -*-
# __author__ = '磊'
from django.shortcuts import render_to_response
from gauth.userManager import UserManager
from gauth.common import MyJSONEncoder
from django.http import HttpResponse
from gauth.models import User
import json


def index(request):
    return render_to_response('admin/user/index.html',{})


def edit(request, user_id):
    if int(user_id) != 0:
        usermanager = UserManager()
        user = usermanager.get_bypk(user_id)

        return render_to_response('admin/user/edit.html',{'user_id':user_id,'user':user})

    return render_to_response('admin/user/edit.html',{'user_id':0})


def update(request):
    from forms import UserForm
    userf = UserForm(request.POST)

    if userf.is_valid() and userf.cleaned_data['password'] == userf.cleaned_data['repassword']:
        user = User()
        user.username = userf.cleaned_data['username']
        user.email = userf.cleaned_data['email']
        user.is_active = userf.cleaned_data['is_active']
        user.nickname = userf.cleaned_data['nickname']
        user.password = userf.cleaned_data['password']
        user.phone = userf.cleaned_data['phone']
        user.id = userf.cleaned_data['id']

        usermanager = UserManager()
        if user.id is None or user.id == 0:
            if usermanager.add(user):
                newuser = usermanager.get_one(user.username)
                res = {'success':True,'pk':newuser.id}
            else:
                res = {'success':False}
        else:
            if usermanager.update(user):
                res = {'success':True,'pk':user.id}
            else:
                res = {'success':False}
    else:
        res = {'success':False,'message':userf.errors}

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def update_user_disable(request, user_id):
    return _update_state(int(user_id),False)


def update_user_enable(request, user_id):
    return _update_state(int(user_id),True)


def _update_state(pk, is_active):
    usermanager = UserManager()
    if usermanager.update_is_active(pk, is_active):
        res = {'success':True}
    else:
        res = {'success':False}

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def users_data(request):
    from forms import PageForm
    pagef = PageForm(request.POST)
    if pagef.is_valid():
        start = pagef.cleaned_data['start']
        length = pagef.cleaned_data['length']
        draw = pagef.cleaned_data['draw']

        usermanager = UserManager()
        users = usermanager.get(start, length)
        count = usermanager.get_count()
    else:
        users = None
        draw = 0
        count = 0

    res= _load_data(users,draw,count)

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def _load_data(users, draw, count):
    ulen = len(users)
    res = {}
    res['draw'] = draw
    res['data'] = []
    res['recordsFiltered'],res['recordsTotal'] = count,count
    for i in range(ulen):
        row = []
        row.append('<input type="checkbox" name="id" value="'+str(users[i].pk)+'">')
        row.append(i+1)
        row.append(users[i].username)
        row.append(users[i].password)
        row.append(users[i].nickname)
        row.append(users[i].email)
        row.append(users[i].phone)
        row.append(users[i].create_time)
        row.append(users[i].last_login_time)
        if users[i].is_active:
            row.append('<span class="label label-sm label-success">正常</span>')
        else:
            row.append('<span class="label label-sm label-default">禁用</span>')

        action = '<a href="javascript:;" data-id="'+str(users[i].pk)+'" class="btn btn-xs default btn-editable"><i class="fa fa-pencil"></i> 编辑</a>'
        if users[i].is_active:
            action += '&nbsp;&nbsp;<a href="javascript:;" data-toggle="confirmation" data-id="'+str(users[i].pk)+'" class="btn btn-xs default btn-disable"><i class="fa  fa-lock"></i>禁用</a>'
        else:
            action += '&nbsp;&nbsp;<a href="javascript:;" data-toggle="confirmation" data-id="'+str(users[i].pk)+'" class="btn btn-xs default btn-enable"><i class="fa fa-unlock-alt"></i>启用</a>'

        row.append(action)

        res['data'].append(row)

    return res