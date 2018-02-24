#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web


class NotFoundHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.set_status(404)
        self.render("index.html", notfound=True)
