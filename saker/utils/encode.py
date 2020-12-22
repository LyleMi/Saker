#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
from urllib.parse import quote
from urllib.parse import unquote


def toBytes(s):
    if isinstance(s, str):
        s = s.encode()
    return s


def toStr(s):
    if isinstance(s, bytes):
        s = s.decode()
    return s


def b64e(s):
    s = toBytes(s)
    return base64.b64encode(s).decode()


def b64d(s):
    '''
    auto handle url encode / url safe base64
    '''
    s = toStr(s)
    if '%' in s:
        s = unquote(s)
    if '-' in s or '_' in s:
        s = s.replace('-', '+').replace('_', '/')
    if len(s) % 4 != 0:
        s += '=' * (len(s) % 4)
    return base64.b64decode(s)


def decodeURL(s):
    return unquote(s)


def doubleURL(s):
    return quote(quote(s))


def hex(s):
    return toBytes(s).hex()


def unhex(s):
    return bytes.fromhex(s).decode()
