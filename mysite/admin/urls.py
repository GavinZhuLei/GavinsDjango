# -*- coding: utf-8 -*-
#__author__ = '磊'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$','admin.login.login'),
    url(r'^index/$','admin.home.index'),
    url(r'^register/$','admin.login.register'),
    url(r'^logout/$', 'admin.login.logout'),

    # user
    url(r'^user/index/$','admin.user.index'),
    url(r'^user/data/$', 'admin.user.users_data'),
    url(r'^user/edit/(?P<user_id>\d+)/$', 'admin.user.edit'),
    url(r'^user/update/$','admin.user.update'),
    url(r'^user/disable/(?P<user_id>\d+)/$', 'admin.user.update_user_disable'),
    url(r'^user/enable/(?P<user_id>\d+)/$', 'admin.user.update_user_enable'),

    # group
    url(r'^group/index/$', 'admin.group.index'),
    url(r'^group/data/$', 'admin.group.group_data'),
    url(r'^group/edit/(?P<group_id>\d+)/$', 'admin.group.edit'),

    url(r'^home/test$', 'admin.home.test'),
    url(r'^home/test1$', 'admin.home.test1'),
    url(r'^home/test2$', 'admin.home.test2'),
    url(r'^login/test$','admin.login.test'),
    url(r'^test/ajax/$', 'admin.home.ajax_page'),
    url(r'^test/ajax_data/$', 'admin.home.ajax_data'),
    url(r'^test/modals/$', 'admin.home.modals'),
)
