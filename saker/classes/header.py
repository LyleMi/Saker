#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.utils.common import randua


class HeaderHelper(object):

    """heap generate Header"""

    def __init__(self, cookie="", ua="", json=False):
        super(HeaderHelper, self).__init__()
        self.headers = {}
        if cookie:
            self.setcookie(cookie)
        if ua:
            self.setua(ua)
        if json:
            self.setjson()

    def setcookie(self, cookie=""):
        self.headers["Cookie"] = cookie if cookie else self.cookie

    def setjson(self):
        self.headers["Content-type"] = "application/json"

    def setua(self, headers={}, UA=""):
        self.headers["User-Agent"] = UA if UA else randua()

    def get(self):
        return self.headers
