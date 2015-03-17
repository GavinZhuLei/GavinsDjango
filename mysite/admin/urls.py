# -*- coding: utf-8 -*-
#__author__ = '磊'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login$','admin.login.login'),
    url(r'^index$','admin.home.index'),
    url(r'^register$','admin.login.register'),
    url(r'^logout$', 'admin.login.logout'),

    url(r'^home/test$', 'admin.home.test'),
    url(r'^home/test1$', 'admin.home.test1'),
    url(r'^home/test2$', 'admin.home.test2'),
    url(r'^login/test$','admin.login.test'),
)
