# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
"""
菜单业务逻辑模块
"""
from models import Menu


def __get_menu(parent_id):
    return Menu.objects.select_related().filter(parent_menu=parent_id).order_by('sort')


def get_all():
    """
    获取配置菜单数据
    :return:
    """
    root_menus = __get_menu(0)
    for root in root_menus:
        if not root.is_leaft:
            # root['child_menu'] = __get_menu(root.pk)
            root.__dict__['child_menu'] = __get_menu(root.pk)
    return root_menus

