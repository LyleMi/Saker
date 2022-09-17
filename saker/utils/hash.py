#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import itertools
import string
try:
    import proofofwork
except Exception as e:
    pass

charset = string.printable[:-5]


def ensure_bytes(s):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return s


def md5(s):
    return hashlib.md5(ensure_bytes(s)).hexdigest()


def sha1(s):
    return hashlib.sha1(ensure_bytes(s)).hexdigest()


def sha512(s):
    return hashlib.sha512(ensure_bytes(s)).hexdigest()


def collision(prefix, suffix='', salt='', pepper='', func=md5):
    for k in range(1, len(charset) + 1):
        for i in itertools.combinations(charset, k):
            s = ''.join(i)
            h = func(salt + s + pepper)
            if h.startswith(prefix) and h.endswith(suffix):
                return s
    return False
