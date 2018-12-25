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
        while len(self.res) < 1:
            pwd = self.queue.get()
            print "try %s" % pwd, "\r"
            try:
                self.zfile.extractall(pwd=pwd)
                res.append(arg)
                break
            except RuntimeError as e:
                pass
            except Exception as e:
                print(e)

    def autorun(self):
        from saker.utils.paths import Paths
        self.run()
        with open(Paths.passwords, "rb") as fh:
            for i in fh:
                self.feed(i.strip("\n"))
        print(self.finish())


if __name__ == '__main__':
    z = Zip("test.zip")
    z.autorun()
