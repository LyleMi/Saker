#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random

from saker.brute.dir import DirBrute
from saker.core.sess import Sess
from saker.handler.headerHandler import HeaderHandler
from saker.handler.htmlHandler import HTMLHandler
from saker.handler.wappalyzer import Wappalyzer
from saker.utils.hash import md5


class Scanner(Sess):

    def __init__(self, *args, **kwargs):
        super(Scanner, self).__init__(*args, **kwargs)
        self.w = Wappalyzer()

    def appinfo(self):
        self.get()
        webpage = self.w.analyze(self.lastr)
        return webpage.info()

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
        return False

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
