#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.brute.brute import Brute
from saker.utils.paths import Paths


class DirBrute(Brute):

    def __init__(self, ext, filename):
        super(DirBrute, self).__init__()
        self.filename = filename
        self.ext = ext

    def weakfiles(self):
        rets = []
        with open(Paths.weakfile) as pathes:
            for p in pathes:
                path = p.strip()
                if "%ext%" in path:
                    path = path.replace("%ext%", self.ext)
                elif "%filename_without_ext%" in path:
                    if not self.filename:
                        continue
                    path = path.replace(
                        "%filename_without_ext%",
                        ".".join(self.filename.split(".")[:-1])
                    )
                elif "%filename%" in path:
                    if not self.filename:
                        continue
                    path = path.replace("%filename%", self.filename)
                rets.append(path)
        return rets

    def senpath(self):
        rets = []
        with open(Paths.senpath) as pathes:
            for p in pathes:
                path = p.strip("\n")
                if "%ext%" in path:
                    path = path.replace("%ext%", self.ext)
                rets.append(path)
        return rets

    def all(self, wf=True, spath=True):
        rets = []
        if wf:
            rets.extend(self.weakfiles())
        if spath:
            rets.extend(self.senpath())
        return rets
