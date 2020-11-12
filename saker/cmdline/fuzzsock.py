#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import argparse

from saker.core.sock import autoSock
from saker.fuzzers.fuzzer import Fuzzer
from saker.fuzzers.dos import DoS
from saker.utils.show import hexdump
from saker.utils.show import clearScreen
from saker.utils.mtime import Timer


def fuzzsock(args):
    parser = argparse.ArgumentParser(
        description="Saker Socket Fuzzer",
        usage="[options]",
        epilog="Fuzz for socket"
    )
    parser.add_argument(
        "-t", "--type",
        default="tcp", dest="type",
        help="define scan type, tcp/udp, use tcp as default"
    )
    parser.add_argument(
        "-p", "--port",
        type=int, dest="port", help="scan port scope"
    )
    parser.add_argument(
        "-a", "--addr",
        dest="addr", help="define fuzz addr"
    )
    opts = parser.parse_args(args)
    if not opts.addr or not opts.port:
        parser.print_help()
        return
    t = Timer()
    for i in range(100):
        clearScreen()
        t.start()
        sock = autoSock(opts.addr, opts.port, opts.type)
        data = Fuzzer.randomBytes(random.randint(100, 1024))
        hexdump(data)
        sock.send(data)
        # DoS.slowWrite(sock, data)
        print(sock.recv(1024))
        t.end()
