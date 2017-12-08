#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
from saker.brute.brute import Brute


class ZipFile(Brute):

    '''
    brute test for http basic auth
    '''

    def __init__(self, zipPath):
        super(ZipFile, self).__init__()
        self.zfile = zipfile.ZipFile(zipPath)

    def do(self, args, res):
        if len(res) > 0:
            return
        try:
            self.zfile.extractall(pwd=args)
            res.append(args)
        except:
            pass
