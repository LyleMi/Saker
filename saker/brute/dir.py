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
        with open(Paths.weakfile) as pathes:
            for p in pathes:
                path = p.strip("\n")
                if "%ext%" in path:
                    path = path.replace("%ext%", self.ext)
                elif "%filename_without_ext%" in path:
                    if not self.filename:
                        continue
                    path = path.replace(
                        "%filename%",
                        ".".join(self.filename.split(".")[:-1])
                    )
                elif "%filename%" in path:
                    if not self.filename:
                        continue
                    path = path.replace("%filename%", self.filename)
                yield path
