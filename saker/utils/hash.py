#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import itertools
import string

charset = string.printable[:-5]


def md5(s):
    return hashlib.md5(s.encode('utf8')).hexdigest()


def collision(prefix, suffix='', func=md5):
    for k in range(1, len(charset) + 1):
        for i in itertools.permutations(charset, k):
            s = ''.join(i)
            h = func(s)
            if h.startswith(prefix) and h.endswith(suffix):
                return s
    return False
