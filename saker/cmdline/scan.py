#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from saker.core.scaner import Scanner

def scan(args):
    parser = argparse.ArgumentParser(
        description='Saker Scanner',
        usage='[options]',
        epilog='Scanner For Website'
    )
    parser.add_argument(
        '-s', '--scan', action="store_true",
        help='run with list model'
    )
    parser.add_argument(
        '-f', '--file', metavar='file',
        default='',
        help='scan specific file'
    )
    parser.add_argument(
        '-e', '--ext', metavar='ext',
        default='php',
        help='scan specific ext'
    )
    parser.add_argument(
        '-i', '--info', action="store_true",
        help='get site info'
    )
    parser.add_argument(
        "-u", '--url',
        dest="url", help="define specific url"
    )
    parser.add_argument(
        "-p", '--proxy',
        dest="proxy", help="proxy url"
    )
    parser.add_argument(
        "-t", '--timeinterval', type=float,
        dest="interval",
        help="scan time interval, random sleep by default",
        default=-1
    )

    opts = parser.parse_args(args)

    url = opts.url

    if not url:
        parser.print_help()
        return

    c = Scanner(url)

    if opts.proxy:
        c.setProxies(opts.proxy)

    if opts.scan or opts.file:
        c.scan(
            filename=opts.file,
            interval=opts.interval,
            ext=opts.ext,
            scan=opts.scan
        )

    if opts.info:
        pprint(c.appinfo())
