#__author__ = 'root'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$','test2.views.index',name='index'),
)