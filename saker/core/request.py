#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
from saker.utils.color import red, cyan, green
from saker.utils.hash import md5


class Request(object):

    def __init__(self, options={}, sess=None):
        """Summary

        Args:
            sess (requests.sessions.Session): request Session
            options (saker.core.Request): request object
        """
        super(Request, self).__init__()
        if sess is None:
            self.sess = requests.Session()
        else:
            self.sess = sess
        self.method = options.get('method', 'get').lower()
        if not self.method:
            self.method = 'get'
        self.url = options.get('url', '')
        self.params = options.get('params', {})
        self.data = options.get('data', {})
        self.files = options.get('files', {})
        self.headers = options.get('headers', {})
        self.cookies = options.get('cookies', {})
        self.interval = 0
        self.lastr = None

    def submit(self):
        start = time.time()
        try:
            self.lastr = getattr(self.sess, self.method)(
                self.url, params=self.params, data=self.data, files=self.files,
                headers=self.headers, cookies=self.cookies
            )
        except Exception as e:
            print(repr(e))
        self.interval = round(time.time() - start, 2)
        return self.lastr

    def brief(self):
        if self.lastr is None:
            return "Exception"
        msg = "\t".join(map(str, [
            self.lastr.status_code,
            len(self.lastr.content),
            self.interval,
            md5(self.lastr.content)[:8]
        ]))
        if self.lastr.status_code // 100 == 5:
            return red(msg)
        elif self.lastr.status_code // 100 == 4:
            return cyan(msg)
        elif self.lastr.status_code // 100 == 3:
            return green(msg)
        else:
            return msg
