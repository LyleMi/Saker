#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.options
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")


class ExitHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")
        exit()


def getApp(debug=True, handlers=[(r"/", MainHandler), (r"/exit", ExitHandler)]):
    # enable looger
    tornado.options.parse_command_line()
    return tornado.web.Application(handlers, debug=debug)


def recordRequest(request):
    print("""%s %s %s\n%s\n%s""" % (
        request.method,
        request.path,
        request.version,
        request.headers,
        request.body.decode(),
    ))


def start(app, port=8888):
    # app.add_handlers(r".*$", handlers)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start(getApp())
