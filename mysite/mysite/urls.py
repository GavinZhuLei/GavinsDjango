# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^test/',include('test.urls')),
    url(r'^test2/', include('test2.urls')),
    url(r'^auth', include('auth.urls')),

    url(r'^admin/index$', 'admin.login.index'),
    url(r'^admin/login$', 'admin.login.login'),
    url(r'^admin/test', 'admin.login.test'),
)

#访问静态文件配置（debug=true）
urlpatterns += staticfiles_urlpatterns()
