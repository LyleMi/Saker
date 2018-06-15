#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.options
import tornado.ioloop
import tornado.web

import server.controller.error

DEBUG = True


tornado.options.define(
    "port", default=8888,
    help="Run server on a specific port", type=int
)

tornado.options.define(
    "host", default="localhost",
    help="Run server on a specific host"
)

tornado.options.define("url", default=None,
                       help="Url to show in HTML"
                       )

tornado.options.parse_command_line()

if not tornado.options.options.url:
    tornado.options.options.url = "http://%s:%d" % (
        tornado.options.options.host, tornado.options.options.port)


settings = {
    "base_url": tornado.options.options.url,
    "template_path": "server/static",
    "cookie_secret": "hsdguouiygruguinksf",
    "compress_response": True,
    "default_handler_class": server.controller.error.NotFoundHandler,
    "xsrf_cookies": False,
    "static_path": "server/static",
}

# 路由
handlers = [
    (r"/", "server.controller.main.MainHandler"),
]
