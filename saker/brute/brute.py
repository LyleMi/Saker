#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import itertools

from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Queue
from multiprocessing import cpu_count


class Brute(object):

    def __init__(self):
        super(Brute, self).__init__()
        self.manager = Manager()
        self.res = self.manager.list()
        self.queue = Queue()
        self.cpuCount = cpu_count()

    @staticmethod
    def itert(start=1, end=0, charset=""):
        if not charset:
            charset = string.printable[:-5]
        if end == 0:
            end = len(charset) + 1
        for k in range(start, end):
            for i in itertools.product(charset, repeat=k):
                s = ''.join(i)
                yield s

    def feed(self, data):
        self.queue.put(data)

    def do(self):
        '''
        multi processing test
        '''
        from time import sleep
        from random import randint
        arg = self.queue.get()
        sleep(randint(1, 5))
        print("here is the %d process, now res is %s" % (arg, self.res))
        self.res.append(arg)

    def run(self, num=-1):
        '''
        args: list contain paramters passed to self.do
              every argument will start a process
        '''
        if num < 0:
            num = self.cpuCount
        self.processes = [
            Process(
                target=self.do,
                args=()
            )
            for i in range(num)
        ]
        for p in self.processes:
            p.start()

    def finish(self):
        for p in self.processes:
            p.join()
        return self.res


if __name__ == '__main__':
    b = Brute()
    b.run(10)
    for i in range(10):
        b.feed(i)
    print(b.finish())
