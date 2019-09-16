#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from saker.servers.http.base import getApp
from saker.servers.http.base import recordRequest
from saker.servers.http.base import start as baseStart


class XSSHandler(tornado.web.RequestHandler):
    def get(self):
        recordRequest(self.request)
        self.write()


def start(host=r".*$", port=8888, handlers=[(r"/xss", SSRFHandler)]):
    app = getApp()
    app.add_handlers(host, handlers)
    baseStart(app, port)


if __name__ == '__main__':
    start()
