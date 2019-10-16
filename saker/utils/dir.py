#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def traverse(path):
    for i in os.listdir(path):
        tmp = os.path.join(path, i)
        if os.path.isdir(tmp):
            for p in traverse(tmp):
                yield p
        elif os.path.isfile(tmp):
            yield tmp
