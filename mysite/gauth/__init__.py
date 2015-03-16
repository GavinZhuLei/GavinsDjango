# -*- coding: utf-8 -*-
# _author = 'Gavin'
from gauth.models import AnonymousUser
from gauth.userManager import UserManager

SESSION_KEY = '_auth_user_id'


def login(request, user):
    request.session[SESSION_KEY] = user.pk
    if hasattr(request, 'user'):
        request.user = user


def get_userpk(request):
    return request.session[SESSION_KEY]


def get_user(request):
    try:
        usermanager = UserManager()
        pk = int(request.session[SESSION_KEY])
        user = usermanager.get_bypk(pk)
        if user is not None:
            return user
        return user or AnonymousUser()
    except:
        return None