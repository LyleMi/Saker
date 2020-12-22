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
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


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
    return int(str2time(today(), "%Y-%m-%d"))


def str2time(s, timeFormat="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(s, timeFormat))


def time2str(t, timeFormat=ISOTIMEFORMAT):
    if isinstance(t, str):
        t = float(t)
    if t > 10000000000:
        # 过大可能是毫秒为单位
        t /= 1000
    return time.strftime(timeFormat, time.localtime(t))


def weekday():
    return datetime.datetime.now().isoweekday()


class Timer(object):

    def __init__(self):
        super(Timer, self).__init__()

    def start(self):
        self.starttime = time.time()

    def end(self):
        print(time.time() - self.starttime)
