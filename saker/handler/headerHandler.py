#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.utils.common import randua


class HeaderHandler(object):

    """help generate Header"""

    def __init__(self, headers={}):
        super(HeaderHandler, self).__init__()
        self.headers = headers

    def set(self, key, value):
        self.headers[key] = value

    def setcookie(self, cookie=""):
        self.headers["Cookie"] = cookie

    def setjson(self):
        self.headers["Content-type"] = "application/json"

    def setua(self, UA=""):
        self.headers["User-Agent"] = UA if UA else randua()

    def setajax(self):
        self.headers["X-Requested-With"] = "XMLHttpRequest"

    def setRefer(self, refer):
        self.headers["Referer"] = refer

    def setXForwardFor(self, ip):
        self.headers["X-Forwarded-For"] = ip

    def show(self):
        print("-" * 100)
        for k in self.headers:
            tmp = "| %s : %s" % (k, self.headers[k])
            if len(tmp) > 100:
                tmp = tmp[:95] + "..."
            tmp = tmp.ljust(98, " ") + " |"
            print(tmp)
        print("-" * 100)
