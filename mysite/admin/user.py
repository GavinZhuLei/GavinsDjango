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


def users_data(request):
    usermanager = UserManager()
    users = usermanager.get_all
    draw = request.POST['draw']
    res= _load_data(users,draw)

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def _load_data(users, draw):
    ulen = len(users)
    res = {}
    res['draw'] = draw
    res['data'] = []
    res['recordsFiltered'],res['recordsTotal'] = ulen,ulen
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

        row.append('<a href="javascript:;" data-id="'+str(users[i].pk)+'" class="btn btn-xs default btn-editable"><i class="fa fa-pencil"></i> 编辑</a>')

        res['data'].append(row)

    return res