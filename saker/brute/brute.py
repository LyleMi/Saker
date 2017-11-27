#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import itertools


class Brute(object):

    def __init__(self):
        super(Brute, self).__init__()

    @staticmethod
    def itert(self, start=1, end=0, charset=""):
        if not charset:
            charset = string.printable[:-5]
        if end == 0:
            end = len(charset) + 1
        for k in range(start, end):
            for i in itertools.permutations(charset, k):
                s = ''.join(i)
                yield s
