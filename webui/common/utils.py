#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import time


def guid():
    return uuid.uuid4().hex


def now():
    # 返回当前时间
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
