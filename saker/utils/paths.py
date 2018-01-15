#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as op


class Paths(object):

    base = op.dirname(
        op.dirname(op.abspath(__file__))
    )
    dirs = op.join(base, "data", "dir.txt")
    linuxfile = op.join(base, "data", "linuxfile.txt")
    passwords = op.join(base, "data", "passwords.txt")
    uas = op.join(base, "data", "user-agents.txt")
    weakfile = op.join(base, "data", "weakfile.txt")


if __name__ == '__main__':
    print Paths.base
