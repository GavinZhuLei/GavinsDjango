# -*- coding: utf-8 -*-
# __author__ = '磊'

from django.db import models
import datetime


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    last_login_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True


class PermissionGroup(models.Model):
    name = models.CharField(max_length=200)
    module = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    action_group = models.ForeignKey(PermissionGroup)

    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    create_username = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    users = models.ManyToManyField(User)
    permission = models.ManyToManyField(Permission)

    def __unicode__(self):
        return self.name