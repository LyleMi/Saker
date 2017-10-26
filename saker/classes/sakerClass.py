#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests

from saker.classes.prettytable import PrettyTable
from saker.utils.domain import parseUrl
from saker.utils.logger import logger
from saker.utils.mprint import printHeader
from saker.utils.paths import fuzztxt


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

    def get(self, path, params={}, headers={}, proxies={},
            timeout=None, verify=None, useSession=True,
            pCode=False, pHeader=False, pContent=False):
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

        if pCode:
            print r.status_code
        if pHeader:
            printHeader(r.headers)
        if pContent:
            print r.content
        return r

    def post(self, path, params={}, data={},
             proxies={}, headers={}, timeout=None,
             verify=None, useSession=True,
             pHeader=False, pContent=False):
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
        if pHeader:
            printHeader(r.headers)
        if pContent:
            self.log(r.content)
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
        exists = []
        x = PrettyTable()
        x._set_field_names(["Path", "Status", "Len"])
        x.align["Path"] = "l"
        with open(fuzztxt) as pathes:
            for p in pathes:
                path = p.strip("\n")
                if "%ext%" in path:
                    path = path.replace("%ext%", ext)
                elif "%filename%" in path:
                    if not filename:
                        continue
                    path = path.replace("%filename%", filename)
                time.sleep(interval)
                try:
                    r = self.get(path)
                    x.add_row([path, r.status_code, len(r.content)])
                    if r.status_code < 400:
                        exists.append(path)
                except Exception as e:
                    print "error while scan", e
        print x.get_string()
        self.log("exists")
        self.log(exists)
