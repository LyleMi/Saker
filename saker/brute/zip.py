#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zipfile import ZipFile
from saker.brute.brute import Brute


class Zip(Brute):

    """brute test for http basic auth
    """

    def __init__(self, zipPath):
        super(Zip, self).__init__()
        self.zfile = ZipFile(zipPath)

    def do(self, arg, res):
        if len(res) > 0:
            return
        try:
            self.zfile.extractall(pwd=arg)
            res.append(arg)
        except:
            pass


if __name__ == '__main__':
    from saker.utils.paths import Paths
    args = []
    with open(Paths.passwords, "rb") as fh:
        for i in fh:
            args.append(i.strip("\n"))
    z = Zip("test.zip")
    z.run(args)
    print(z.res)
