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

    def do(self):
        while len(self.res) < 0 and self.queue.get():
            pwd = self.queue.get()
            print("try %s" % pwd)
            try:
                self.zfile.extractall(pwd=pwd)
                res.append(arg)
                break
            except:
                pass


if __name__ == '__main__':
    from saker.utils.paths import Paths
    z = Zip("test.zip")
    args = range(5)
    z.run(args)
    with open(Paths.passwords, "rb") as fh:
        for i in fh:
            z.feed(i.strip("\n"))
    print(z.res)
