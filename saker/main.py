#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import random
import requests

from saker.brute.dir import DirBrute
from saker.handler.headerHandler import HeaderHandler
from saker.handler.htmlHandler import HTMLHandler
from saker.utils.domain import parseUrl
from saker.utils.logger import logger


class Saker(object):

    cookie = ""
    proxies = {}
    timeout = 20
    verify = False

    def __init__(
            self, url="", session=None,
            timeout=0, loglevel="debug"
    ):
        """
        :param s: store requests session
        :param url: main url
        """
        super(Saker, self).__init__()
        if session is not None:
            self.s = session
        else:
            self.s = requests.Session()
        if timeout != 0:
            self.timeout = timeout
        self.url = parseUrl(url)
        self.loglevel = loglevel
        self.logger = logger
        self.lastr = None
        self.trace = False

    def traceRequest(self):
        print(self.lastr.request.headers)
        print(self.lastr.headers)
        print(self.lastr.content)
        print(self.lastr.history)

    def get(self, path="", *args, **kwargs):
        self.lastr = self.s.get(self.url + path, *args, **kwargs)
        return self.lastr

    def post(self, path="", *args, **kwargs):
        self.lastr = self.s.post(self.url + path, *args, **kwargs)
        return self.lastr

    def put(self, path="", *args, **kwargs):
        self.lastr = self.s.put(self.url + path, *args, **kwargs)
        return self.lastr

    def patch(self, path="", *args, **kwargs):
        self.lastr = self.s.patch(self.url + path, *args, **kwargs)
        return self.lastr

    def delete(self, path="", *args, **kwargs):
        self.lastr = self.s.delete(self.url + path, *args, **kwargs)
        return self.lastr

    def trace(self):
        '''trace http redirect
        '''
        if self.lastr is not None and self.lastr.history:
            for r in self.lastr.history:
                print(r.url)
            print(self.lastr.url)

    def interactive(self):
        while True:
            cmd = raw_input(">>> ")
            if cmd in ["exit", "quit"]:
                return
            elif cmd == "set":
                key = input(">>> set what? : ")
                value = input(">>> vaule? : ")
                self.__setattr__(key, value)
                print("set self.%s with value %s" % (key, self.__getattribute__(key)))
                continue
            try:
                call = self.__getattribute__(cmd)
            except AttributeError as e:
                print("has no attribute " + cmd)
                continue
            if callable(call):
                call()
            else:
                print(call)

    def mirror(self, path=""):
        '''
        mirror current site
        '''
        self.get(path)
        with open("index.html", "wb") as fh:
            fh.write(self.lastr.content)
        links = HTMLHandler(self.lastr.text).links
        for link in links:
            if link.startswith("http") or link.startswith("//"):
                continue
            dirs = link.split("/")
            if dirs[0] == "":
                dirs = dirs[1:]
            for d in range(1, len(dirs)):
                if not os.path.exists(os.path.sep.join(dirs[:d])):
                    print("path [%s]" % os.path.sep.join(dirs[:d]))
                    os.mkdir(os.path.sep.join(dirs[:d]))
            self.get(link)
            with open(os.path.sep.join(dirs), "wb") as fh:
                fh.write(self.lastr.content)

    def setProxies(self, proxies):
        if isinstance(proxies, dict):
            self.s.proxies = proxies
        elif isinstance(proxies, str):
            self.s.proxies = {
                "http": proxies,
                "https": proxies,
            }

    def setUA(self, UA=""):
        from saker.utils.common import randua
        self.s.headers["User-Agent"] = UA if UA else randua()

    def scan(self, ext="php", filename="", interval=0, scan=True):
        '''
        small scan
        scan url less than 100
        and get some base info of site
        '''
        self.get("")
        HeaderHandler(self.lastr.headers).show()
        exists = []
        dirBrute = DirBrute(ext, filename)
        for path in dirBrute.all(filename, scan):
            if interval == -1:
                time.sleep(random.randint(1, 5))
            else:
                time.sleep(interval)
            try:
                r = self.get(path)
                content = HTMLHandler(r.text)
                print("%s - %s - /%s\t%s" % (
                    r.status_code,
                    content.size,
                    path,
                    content.title
                ))
                if r.status_code < 400:
                    exists.append(path)
            except Exception as e:
                print("error while scan %s" % e)
        self.logger.info("exists %s" % exists)


if __name__ == '__main__':

    import sys
    import argparse

    from saker.data.banner import banner

    parser = argparse.ArgumentParser(
        description='Tool For Fuzz Web Applications',
        usage='%(prog)s [options]',
        epilog='Tool For Fuzz Web Applications')
    parser.add_argument('-s', '--scan', action="store_true",
                        help='run with list model')
    parser.add_argument('-f', '--file', metavar='file',
                        default='',
                        help='scan specific file')
    parser.add_argument('-e', '--ext', metavar='ext',
                        default='php',
                        help='scan specific ext')
    parser.add_argument('-i', '--interactive', action="store_true",
                        help='run with interactive model')
    parser.add_argument("-u", '--url',
                        dest="url", help="define specific url")
    parser.add_argument("-p", '--proxy',
                        dest="proxy", help="proxy url")
    parser.add_argument("-t", '--timeinterval', type=float,
                        dest="interval",
                        help="scan time interval, random sleep by default",
                        default=-1)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        sys.stderr.write('Url is required!')
        sys.exit(1)

    print(banner)

    c = Saker(url)

    if opts.proxy:
        c.setProxies(opts.proxy)

    if opts.scan or opts.file:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext,
               scan=opts.scan)

    if opts.interactive:
        c.interactive()
