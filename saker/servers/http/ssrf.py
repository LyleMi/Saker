#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from saker.servers.http.base import getApp
from saker.servers.http.base import recordRequest
from saker.servers.http.base import start as baseStart

class SSRFHandler(tornado.web.RequestHandler):
    def get(self):
        recordRequest(self.request)
        scheme = self.get_argument('s', 'http')
        ip = self.get_argument('i', '127.0.0.1')
        port = self.get_argument('p', '80')
        path = self.get_argument('path', '')
        code = self.get_argument('code', '301')
        self.redirect(scheme + '://' + ip + ':' + port + path, status=int(code))


def start(host=r".*$", port=8888, handlers=[(r"/ssrf", SSRFHandler)]):
    app = getApp()
    app.add_handlers(host, handlers)
    baseStart(app, port)

if __name__ == '__main__':
    start()
