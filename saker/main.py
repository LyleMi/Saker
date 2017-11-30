#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def __init__(self, url="", session=None, timeout=0, loglevel="debug"):
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

    def get(self, path="", params={}, headers={}, proxies={},
            timeout=None, verify=None, useSession=True):
        if timeout is None:
            timeout = self.timeout
        if verify is None:
            verify = self.verify

        if useSession:
            r = self.s.get(self.url + path, params=params,
                           headers=headers, timeout=timeout,
                           proxies=proxies, verify=verify)
        else:
            r = requests.get(self.url + path, params=params,
                             headers=headers, timeout=timeout,
                             verify=verify)
        self.lastr = r
        return r

    def post(self, path="", params={}, data={},
             proxies={}, headers={}, timeout=None,
             verify=None, useSession=True):
        if timeout is None:
            timeout = self.timeout
        if verify is None:
            verify = self.verify
        if useSession:
            r = self.s.post(self.url + path, params=params, data=data,
                            headers=headers, timeout=timeout,
                            proxies=proxies, verify=verify)
        else:
            r = requests.post(self.url + path, params=params, data=data,
                              headers=headers, timeout=timeout,
                              verify=verify)
        self.lastr = r
        return r

    def interactive(self):
        while True:
            cmd = raw_input(">>> ")
            if cmd in ["exit", "quit"]:
                return
            elif cmd == "set":
                key = raw_input(">>> set what? : ")
                value = raw_input(">>> vaule? : ")
                self.__setattr__(key, value)
                print "set self.%s with value %s" \
                    % (key, self.__getattribute__(key))
                continue
            try:
                call = self.__getattribute__(cmd)
            except AttributeError, e:
                print "has no attribute " + cmd
                continue
            if callable(call):
                call()
            else:
                print call

    def log(self, msg, level=""):
        if level == "":
            level = self.loglevel
        level = level.lower()

        if level == "verbose":
            pass
        elif level == "debug":
            self.logger.debug(msg)
        elif level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)

    def scan(self, ext="php", filename="", interval=0):
        '''
        small scan
        scan url less than 100
        and get some base info of site
        '''
        self.get("")
        HeaderHandler(self.lastr.headers).show()
        exists = []
        dirBrute = DirBrute(ext, filename)
        for path in dirBrute.brute():
            if interval == -1:
                time.sleep(random.randint(1, 5))
            else:
                time.sleep(interval)
            try:
                r = self.get(path)
                content = HTMLHandler(r.content)
                print "%s - %s - /%s\t%s" % (
                    r.status_code,
                    content.size,
                    path,
                    content.title
                )
                if r.status_code < 400:
                    exists.append(path)
            except Exception as e:
                print "error while scan", e
        self.logger.info("exists %s" % exists)

if __name__ == '__main__':

    import sys
    import argparse

    from saker.data.banner import banner

    parser = argparse.ArgumentParser(
        description='CTF Web fuzz framework',
        usage='%(prog)s [options]',
        epilog='CTF Web fuzz framework')
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
    parser.add_argument("-t", '--timeinterval', type=int,
                        dest="interval",
                        help="scan time interval, random sleep by default",
                        default=-1)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        sys.stderr.write('Url is required!')
        sys.exit(1)

    print banner

    c = Saker(url)

    if opts.scan:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext)

    if opts.interactive:
        c.interactive()
