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
from saker.utils.logger import getLogger
from saker.utils.hash import md5

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Saker(object):

    """Core Scanner

    Attributes:
        ffua (str): Firefox User Agent Str for default UA
        jsonr (TYPE): JSON response
        lastr (TYPE): last response
        s (TYPE): Session
        timeout (int): Default requests timeout
        url (TYPE): Main url

    Deleted Attributes:
        proxies (dict): Description
    """

    # 'Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>'
    ffua = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

    def __init__(
            self, url="", verify=False,
            timeout=0, loglevel="debug"
    ):
        """
        Args:
            url (str, optional): main url
            verify (bool, optional): verify or not
            timeout (int, optional): requests timeout
        """
        super(Saker, self).__init__()
        self.s = requests.Session()
        if timeout != 0:
            self.timeout = timeout
        self.url = parseUrl(url)
        self.loglevel = loglevel
        self.logger = getLogger()
        self.lastr = None
        self.s.verify = verify
        self.setUA(self.ffua)

    def _callback(self):
        """Request Callback
        """
        if 'Content-Type' in self.lastr.headers and self.lastr.headers['Content-Type'] == 'application/json; charset="utf-8"':
            self.jsonLoadr()

    def trace(self):
        """Trace requests
        """
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
        """load json response
        """
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
        """load saved cookie

        Args:
            pkl (str, optional): cookie file name
        """
        self.logger.debug('loading cookie...')
        with open(pkl, 'rb') as f:
            self.s.cookies = pickle.load(f)

    def saveCookie(self, pkl='.cookie.pkl'):
        """save cookie

        Args:
            pkl (str, optional): cookie file name
        """
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
        """set request proxies
        """
        if isinstance(proxies, dict):
            self.s.proxies = proxies
        elif isinstance(proxies, str):
            self.s.proxies = {
                "http": proxies,
                "https": proxies,
            }

    def setUA(self, UA=""):
        """set default User Agent
        """
        from saker.utils.common import randua
        self.s.headers["User-Agent"] = UA if UA else randua()

    def scan(self, ext="php", filename="", interval=0, scan=True):
        '''
        small scan
        scan url less than 100
        and get some base info of site

        Args:
            ext (str, optional): site ext
            filename (str, optional): file to scan
            interval (int, optional): scan interval
            scan (bool, optional): scan or not
        '''
        self.get("")
        self.logger.info('\n' + HeaderHandler(self.lastr.headers).show(True))
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
                self.logger.error("error while scan %s" % e)
        self.logger.info("exists %s" % exists)
        return exists

    def testAll200(self):
        """return True if site always returns 200
        """
        r1 = self.get(md5(random.randint()))
        r2 = self.get(md5(random.randint()) + '/' + md5(random.randint()))
        if r1.status_code == 200 and r2.status_code == 200:
            return True
