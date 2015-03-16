# -*- coding: utf-8 -*-
# _author = 'Gavin'
from gauth.models import AnonymousUser
from gauth.userManager import UserManager


SESSION_KEY = '_auth_user_id'


def login(request, user):
    """
    自己实现的登陆，参考django的auth模块
    :param request:
    :param user:
    :return:
    """
    if user is None:
        user = request.user
    if SESSION_KEY in request.session:
        if request.session[SESSION_KEY] != user.pk:
            request.session.flush()
    else:
        request.session.cycle_key()
    request.session[SESSION_KEY] = user.pk
    if hasattr(request, 'user'):
        request.user = user


def logout(request):
    """
    用户登出，参考django 的auth
    :param request:
    :return:
    """
    user = getattr(request, 'user', None)
    if not user.is_authenticated():
        user = None
    request.session.flush()
    if hasattr(request, 'user'):
        request.user = AnonymousUser()

def get_userpk(request):
    return request.session[SESSION_KEY]


def get_user(request):
    try:
        usermanager = UserManager()
        user_id = request.session[SESSION_KEY]
    except KeyError:
        return AnonymousUser()
    else:
        user = usermanager.get_bypk(user_id)
        return user