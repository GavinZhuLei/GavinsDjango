# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import hashlib


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
