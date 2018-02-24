#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.wsgi
import wsgiref.simple_server

from common.config import DEBUG
from common.config import settings
from common.config import handlers

from common.core import initDB

def main():
    try:
        app = tornado.web.Application(handlers, debug=DEBUG, **settings)
        app.db = initDB()
        print("[*] Server run at %s" % tornado.options.options.url)
        
        if True:
            app.listen(tornado.options.options.port)
            tornado.ioloop.IOLoop.instance().start()
        else:
            # reserve for wsgi
            server = wsgiref.simple_server.make_server('', 8888, app)
            server.serve_forever()
    except Exception as e:
        import traceback
        print(traceback.print_exc())
    finally:
        import sys
        sys.exit(0)

if __name__ == "__main__":
    main()
