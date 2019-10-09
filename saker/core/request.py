#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Request(object):

    def __init__(self, sess=None, options={}):
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

    def submit(self):
        self.lastr = getattr(self.sess, self.method)(
            self.url, params=self.params, data=self.data, files=self.files,
            headers=self.headers, cookies=self.cookies
        )
        return self.lastr

    def brief(self):
        return "%s %s" % (self.lastr.status_code, len(self.lastr.content))
