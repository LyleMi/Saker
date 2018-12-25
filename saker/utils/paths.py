#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as op


class Paths(object):

    base = op.dirname(
        op.dirname(op.abspath(__file__))
    )
    uas = op.join(base, "data", "user-agents.txt")
    sqlkeywords = op.join(base, "data", "sqlkeywords.txt")
    linuxfile = op.join(base, "data", "linuxfile.txt")
    
    dirs = op.join(base, "data", "website", "dir.txt")
    weakfile = op.join(base, "data", "website", "weakfile.txt")
    senpath = op.join(base, "data", "website", "sensitivepath.txt")
    
    subnames = op.join(base, "domains", "subnames.txt")
    usernames = op.join(base, "data", "userpass", "small-user.txt")
    passwords = op.join(base, "data", "userpass", "small-pass.txt")


if __name__ == '__main__':
    print(Paths.base)
