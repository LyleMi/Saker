#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import pickle
import requests

from saker.utils.url import normalizeUrl
from saker.utils.hash import md5
from saker.utils.logger import getLogger
from saker.utils.datatype import AttribDict


class Sess(object):

    """Core Scanner

    Attributes:
        ffua (str): Firefox User Agent Str for default UA
        jsonr (TYPE): JSON response
        lastr (TYPE): last response
        s (TYPE): Session
        timeout (int): Default requests timeout
        url (TYPE): Main url
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
        super(Sess, self).__init__()
        self.s = requests.Session()
        if timeout != 0:
            self.timeout = timeout
        self.url = normalizeUrl(url)
        self.loglevel = loglevel
        self.logger = getLogger()
        self.lastr = None
        self.s.verify = verify
        self.setUA(self.ffua)

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

    def cacheGet(self, path=""):
        cachefile = '.%s.html' % md5(path)
        if os.path.exists(cachefile):
            with open(cachefile, 'rb') as fh:
                return fh.read()
        else:
            self.get(path)
            with open(cachefile, 'wb') as fh:
                fh.write(r.content)
                return r.content

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

    def _callback(self):
        """Request Callback
        """
        if 'Content-Type' in self.lastr.headers and self.lastr.headers['Content-Type'] == 'application/json; charset="utf-8"':
            self.jsonLoadr()

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
