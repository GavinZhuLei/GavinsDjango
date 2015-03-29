# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import hashlib
import json
import datetime
import decimal
from django.core.serializers import serialize,deserialize
from django.core.serializers.json import DjangoJSONEncoder, DateTimeAwareJSONEncoder
from django.db.models.query import QuerySet
from django.db import models
from django.utils.timezone import is_aware


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


def convert_to_int_list(text):
    return [int(i) for i in text.split(',')]


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
        # return DateTimeAwareJSONEncoder.default(o)

        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            o = o + datetime.timedelta(hours=8)
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:10] + ' ' + r[11:-6]
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DjangoJSONEncoder, self).default(o)