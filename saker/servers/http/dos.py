import tornado.web
from saker.servers.http.base import getApp
from saker.servers.http.base import start as baseStart


class RedirectHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/")


def start(host=r".*$", port=8888, handlers=[(r"/", RedirectHandler)]):
    app = getApp(handlers=handlers)
    baseStart(app, port)


if __name__ == '__main__':
    start()
