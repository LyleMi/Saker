#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
from urllib.parse import quote
from urllib.parse import unquote


def b64d(s):
    '''
    auto handle url encode / url safe base64
    '''
    if '%' in s:
        s = unquote(s)
    if '-' in s or '_' in s:
        s = s.replace('-', '+').replace('_', '/')
    if len(s) % 4 != 0:
        s += '=' * (len(s) % 4)
    return base64.b64decode(s)


def doubleURL(s):
    return quote(quote(s))
