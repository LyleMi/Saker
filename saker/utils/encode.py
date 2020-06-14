#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
from urllib.parse import quote
from urllib.parse import unquote


def b64e(s):
    if isinstance(s, str):
        s = s.encode()
    return base64.b64encode(s).decode()


def b64d(s):
    '''
    auto handle url encode / url safe base64
    '''
    if isinstance(s, bytes):
        s = s.decode()
    if '%' in s:
        s = unquote(s)
    if '-' in s or '_' in s:
        s = s.replace('-', '+').replace('_', '/')
    if len(s) % 4 != 0:
        s += '=' * (len(s) % 4)
    return base64.b64decode(s)


def doubleURL(s):
    return quote(quote(s))


def hex(s):
    return s.encode().hex()


def unhex(s):
    return bytes.fromhex(s).decode()
