#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import itertools

from multiprocessing import Process
from multiprocessing import Manager


class Brute(object):

    '''For Windows do not support many feature
    '''
    def __init__(self):
        super(Brute, self).__init__()
        self.res = []

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

    def do(self, arg, res):
        '''
        multi processing test
        '''
        from time import sleep
        from random import randint
        sleep(randint(1, 5))
        print("here is the %d process, now res is %s" % (arg, res))
        res.append(arg)

    def run(self, args):
        '''
        args: list contain paramters passed to self.do
              every argument will start a process
        '''
        manager = Manager()
        res = manager.list()
        processes = [
            Process(
                target=self.do,
                args=(arg, res)
            )
            for arg in args
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        return res

if __name__ == '__main__':
    b = Brute()
    print(b.run(range(10)))
