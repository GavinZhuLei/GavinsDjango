# -*- coding:utf-8 -*-
# __author__ = 'Gavin'
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gauth.common import MyJSONEncoder
from gauth.groupManager import GroupManager

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


def edit(request, group_id):
    if int(group_id) != 0:
        return render_to_response('admin/group/edit.html',{'group_id':0})
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

        action = '<a href="javascript:;" data-id="'+str(groups[i].pk)+'" class="btn btn-xs default btn-editable"><i class="fa fa-pencil"></i> 编辑</a>'

        row.append(action)

        res['data'].append(row)

    return res