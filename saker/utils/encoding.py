#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import quote

def urlencode(s, force=False):
    if not force:
        s = quote(s)
    else:
        s = map(lambda i: hex(ord(i)).replace("0x", "%"), s)
        s = "".join(s)
    return s

if __name__ == '__main__':
    print urlencode("s0!*@#")
    print urlencode("t", True)