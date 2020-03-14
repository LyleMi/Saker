#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from saker.servers.http.base import start as startHTTP

def server(args):
    parser = argparse.ArgumentParser(
        description='Saker Server',
        usage='[options]',
        epilog='Server For Test'
    )
    parser.add_argument(
        '-t', '--type', metavar='type',
        default='',
        help='server type'
    )
    parser.add_argument(
        '-p', '--port', metavar='port',
        default=8888, type=int,
        help='server port'
    )
    opts = parser.parse_args(args)
    if not opts.type:
        parser.print_help()
        return
    if opts.type == 'http':
        startHTTP(port=opts.port)
