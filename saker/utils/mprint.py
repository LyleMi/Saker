#!/usr/bin/env python
# -*- coding: utf-8 -*-

def printHeader(headers):
    print "-" * 100
    for k in headers:
        tmp = "| %s : %s" % (k, headers[k])
        if len(tmp) > 100:
            tmp = tmp[:95] + "..."
        tmp = tmp.ljust(98, " ") + " |"
        print tmp

    print "-" * 100