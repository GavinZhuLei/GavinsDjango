# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gauth.common import MyJSONEncoder
from gauth.groupManager import GroupManager
from gauth.models import Group

def index(request):
    return render_to_response('admin/group/index.html',{})


def group_data(request):
    """
    获取用户组列表数据
    :param request:
    :return:
    """
    from forms import PageForm
    pagef = PageForm(request.POST)
    if pagef.is_valid():
        start = pagef.cleaned_data['start']
        length = pagef.cleaned_data['length']
        draw = pagef.cleaned_data['draw']

        groupmanager = GroupManager()
        users = groupmanager.get(start, length)
        count = groupmanager.get_count()
    else:
        users = None
        draw = 0
        count = 0

    res= _load_data(users,draw,count)

    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def save(request):
    """
    保存用户组信息
    :param request:
    :return:
    """
    from forms import GroupForm
    groupf = GroupForm(request.POST)

    if groupf.is_valid():
        group = Group()
        from datetime import datetime
        group.create_time = datetime.now()
        group.create_username = request.user.username
        group.description = groupf.cleaned_data['description']
        group.is_available = True
        group.name = groupf.cleaned_data['name']
        group.id = groupf.cleaned_data['id']

        groupmanager = GroupManager()
        if group.id is None or group.id == 0:
            if groupmanager.add(group):
                newgroup = groupmanager.get_one_name(group.name)
                res = {'success':True,'pk':newgroup.id}
            else:
                res = {'success':False}
        else:
            if groupmanager.update(group):
                res = {'success':True, 'pk':group.id}
            else:
                res = {'success':False}
    else:
        res = {'success':False,'message':groupf.errors}
    return HttpResponse(json.dumps(res, cls=MyJSONEncoder))


def edit(request, group_id):
    if int(group_id) != 0:
        groupmanager = GroupManager()
        group = groupmanager.get_one_pk(group_id)

        return render_to_response('admin/group/edit.html',{'group_id':group_id, 'group':group})
    return render_to_response('admin/group/edit.html',{'group_id':0})


def _load_data(groups, draw, count):
    glen = len(groups)
    res = {}
    res['draw'] = draw
    res['data'] = []
    res['recordsFiltered'],res['recordsTotal'] = count,count
    for i in range(glen):
        row = []
        row.append('<input type="checkbox" name="id" value="'+str(groups[i].pk)+'">')
        row.append(i+1)
        row.append(groups[i].name)
        row.append(groups[i].description)
        row.append(groups[i].create_username)
        row.append(groups[i].create_time)
        if groups[i].is_available:
            row.append('<span class="label label-sm label-success">有效</span>')
        else:
            row.append('<span class="label label-sm label-default">无效</span>')

        action = '<a href="javascript:;" data-id="'+str(groups[i].pk)+'" class="btn btn-xs default btn-editable"><i class="fa fa-edit"></i> 编辑</a>'

        row.append(action)

        res['data'].append(row)

    return res