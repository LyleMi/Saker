#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import json
import pickle
import random
import urllib3
import requests

from saker.brute.dir import DirBrute
from saker.handler.headerHandler import HeaderHandler
from saker.handler.htmlHandler import HTMLHandler
from saker.utils.datatype import AttribDict
from saker.utils.domain import parseUrl
from saker.utils.logger import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
        self.s.verify = False

    def _callback(self):
        if 'Content-Type' in self.lastr.headers and self.lastr.headers['Content-Type'] == 'application/json; charset="utf-8"':
            self.jsonLoadr()

    def trace(self):
        if self.lastr is None:
            return
        HeaderHandler(self.lastr.request.headers).show()
        HeaderHandler(self.lastr.headers).show()
        print(self.lastr.text)
        if not self.lastr.history:
            return
        for r in self.lastr.history:
            print(r.url)
        print(self.lastr.url)

    def jsonLoadr(self):
        if self.lastr is None:
            return
        try:
            self.jsonr = AttribDict(json.loads(self.lastr.text))
        except json.decoder.JSONDecodeError as e:
            pass
        return self.jsonr

    def get(self, path="", *args, **kwargs):
        self.lastr = self.s.get(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def post(self, path="", *args, **kwargs):
        self.lastr = self.s.post(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def put(self, path="", *args, **kwargs):
        self.lastr = self.s.put(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def patch(self, path="", *args, **kwargs):
        self.lastr = self.s.patch(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def delete(self, path="", *args, **kwargs):
        self.lastr = self.s.delete(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def loadCookie(self, pkl='.cookie.pkl'):
        self.logger.debug('loading cookie...')
        with open(pkl, 'rb') as f:
            self.s.cookies = pickle.load(f)

    def saveCookie(self, pkl='.cookie.pkl'):
        self.logger.debug('save cookie...')
        with open(pkl, 'wb') as f:
            pickle.dump(self.s.cookies, f)

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

