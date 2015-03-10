# -*- coding: utf-8 -*-
# __author__ = '磊'

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    last_login_time = models.DateTimeField()
    # groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.username



# class Group(models.Model):
#     name = models.CharField(max_length=50)
#     create_time = models.DateTimeField()
#     users = models.ManyToManyField(User)
#
#     def __unicode__(self):
#         return self.name
#
#
# class Permission(models.Model):
#     name = models.CharField(max_length=200)
#     action = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.name