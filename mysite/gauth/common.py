# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import hashlib
import json
from django.core.serializers import serialize,deserialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.db import models


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


class MyJSONEncoder(json.JSONEncoder):
    """
    将对象转化成Json对象
    """
    def default(self, o):
        if isinstance(o, QuerySet):
            a = json.loads(serialize('json',o))
            return a
        if isinstance(o, models.Model):
            return json.loads(serialize('json',[o])[1:-1])
        return DjangoJSONEncoder.default(self, o)