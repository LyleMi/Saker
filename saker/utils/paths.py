#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path as op


class Paths(object):

    base = op.dirname(
        op.dirname(op.abspath(__file__))
    )
    names = op.join(base, "data", "names.txt")
    areaid = op.join(base, "data", "areaid.json")
    uas = op.join(base, "data", "user-agents.txt")
    sqlkeywords = op.join(base, "data", "sqlkeywords.txt")
    linuxfile = op.join(base, "data", "linuxfile.txt")
    windowsfile = op.join(base, "data", "windowsfile.txt")

    dirs = op.join(base, "data", "website", "dir.txt")
    weakfile = op.join(base, "data", "website", "weakfile.txt")
    senpath = op.join(base, "data", "website", "sensitivepath.txt")
    webdict = op.join(base, "data", "website", "dict.txt")

    subnames = op.join(base, "domains", "subnames.txt")
    usernames = op.join(base, "data", "userpass", "small-user.txt")
    passwords = op.join(base, "data", "userpass", "small-pass.txt")


def traverse(path, yieldDir=False):
    for i in os.listdir(path):
        tmp = os.path.join(path, i)
        if yieldDir:
            yield tmp, i
        if os.path.isdir(tmp):
            for p in traverse(tmp, yieldDir):
                yield p
        elif os.path.isfile(tmp):
            yield tmp, i


def makeIfNotExists(path):
    paths = path.split(os.sep)
    cur = ""
    for path in paths:
        cur = os.path.join(cur, path)
        if not os.path.exists(cur):
            os.mkdir(cur)


def getUpper(path):
    return os.path.dirname(path)
