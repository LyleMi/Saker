#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import random

from saker.utils.paths import Paths


def randua():
    # 生成随机ua
    return random.choice([i.strip("\n") for i in open(Paths.uas)])


def store(url, obj):
    p = url.split("//")[1].strip("/") + ".pkl"
    # url such as 127.0.0.1:8882 will triger a bug on windows
    p = p.replace(":", "_")
    p = os.path.join(".", "logs", p)
    output = open(p, 'wb')
    pickle.dump(obj, output)
    output.close()


def load(url):
    p = url.split("//")[1].strip("/") + ".pkl"
    p = p.replace(":", "_")
    p = os.path.join(".", "logs", p)
    pklFile = open(p, 'rb')
    data = pickle.load(pklFile)
    pklFile.close()
    return data
