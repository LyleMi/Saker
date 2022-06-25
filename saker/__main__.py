#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import importlib



def main():
    supportActions = [
        "scan",
        "file",
        "fuzz",
        "fuzzsock",
        "port",
        "poc",
        "server",
        "util",
    ]
    if len(sys.argv) > 1 and sys.argv[1] in supportActions:
        module = importlib.import_module("saker.cmdline.%s" % sys.argv[1])
        func = getattr(module, sys.argv[1])
        func(sys.argv[2:])
    else:
        print("unknown command, support %s" % "/".join(supportActions))


if __name__ == '__main__':
    main()
