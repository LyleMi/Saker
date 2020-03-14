#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pprint import pprint
from saker.cmdline.scan import scan
from saker.cmdline.port import port
from saker.cmdline.fuzz import fuzz
from saker.cmdline.server import server


def main():
    if sys.argv[1] == 'scan':
        scan(sys.argv[2:])
    elif sys.argv[1] == 'fuzz':
        fuzz(sys.argv[2:])
    elif sys.argv[1] == 'port':
        port(sys.argv[2:])
    elif sys.argv[1] == 'server':
        server(sys.argv[2:])
    else:
        print('unknown command, support scan / fuzz / port')


if __name__ == '__main__':
    main()
