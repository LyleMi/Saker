#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import datetime

ISOTIMEFORMAT = "%Y-%m-%d %X"


def now():
    # 返回当前时间
    return time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))


def today():
    # 返回今天的时间
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def nowdate():
    return datetime.datetime.now()


def timestr(shift=0):
    return time.strftime(ISOTIMEFORMAT, time.localtime(time.time() + shift))


def pastTime(old, now=None):
    if now is None:
        now = datetime.datetime.now()
    return int((now - old).total_seconds())


def unixnow():
    return int(time.time())


def unixtoday():
    return int(str2time(today()))


def str2time(s):
    return time.mktime(time.strptime(s, "%Y-%m-%d"))


def time2str(t):
    return time.strftime(ISOTIMEFORMAT, time.localtime(t))

if __name__ == '__main__':
    print(unixtoday())
