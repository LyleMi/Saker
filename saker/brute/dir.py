#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.brute.brute import Brute
from saker.utils.paths import fuzzpath


class DirBrute(Brute):

    def __init__(self, ext, filename):
        super(DirBrute, self).__init__()
        self.filename = filename
        self.ext = ext

    def brute(self):
        with open(fuzzpath) as pathes:
            for p in pathes:
                path = p.strip("\n")
                if "%ext%" in path:
                    path = path.replace("%ext%", self.ext)
                elif "%filename%" in path:
                    if not self.filename:
                        continue
                    path = path.replace("%filename%", self.filename)
                yield path