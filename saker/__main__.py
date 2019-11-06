#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from saker.data.banner import banner
from saker.core.scaner import Scanner
from saker.core.mutator import Mutator
from saker.core.request import Request
from saker.utils.url import parseQuery
from saker.utils.url import normalizeUrl


def main():
    if sys.argv[1] == 'scan':
        scanner(sys.argv[2:])
    elif sys.argv[1] == 'fuzz':
        fuzz(sys.argv[2:])


def scanner(args):
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
        '-i', '--interactive', action="store_true",
        help='run with interactive model'
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

    print(banner)

    c = Scanner(url)

    if opts.proxy:
        c.setProxies(opts.proxy)

    if opts.scan or opts.file:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext,
               scan=opts.scan)

    if opts.interactive:
        c.interactive()


def fuzz(args):
    parser = argparse.ArgumentParser(
        description='Saker Fuzzer',
        usage='[options]',
        epilog='Fuzz for web request'
    )
    parser.add_argument(
        "-u", '--url',
        dest="url", help="define specific url"
    )
    parser.add_argument(
        "-m", '--method',
        dest="method", help="request method, use get as default",
        default="get"
    )
    parser.add_argument(
        "-p", '--params',
        dest="params", help="request params, use empty string as default",
        default=""
    )
    parser.add_argument(
        "-d", '--data',
        dest="data", help="request data, use empty string as default",
        default=""
    )
    parser.add_argument(
        '-H', '--headers',
        dest="headers", help="request headers, use empty string as default",
        default=""
    )
    parser.add_argument(
        "-c", '--cookies',
        dest="cookies", help="request cookies, use empty string as default",
        default=""
    )
    parser.add_argument(
        "-P", '--part',
        dest="part", help="fuzz part, could be url / params / data / ...",
        default=""
    )
    parser.add_argument(
        "-k", '--key',
        dest="key", help="key to be fuzzed",
        default=""
    )
    parser.add_argument(
        "-v", '--vuln',
        dest="vuln", help="Vulnarability type to be fuzzed",
        default=""
    )
    parser.add_argument(
        "-t", '--timeinterval', type=float,
        dest="interval",
        help="scan time interval, random sleep by default",
        default=0
    )
    opts = parser.parse_args(args)

    if not opts.url:
        parser.print_help()
        return

    if opts.method.lower() not in ['get', 'post', 'put', 'patch', 'delete']:
        print('method error')
        return

    print(opts.headers)

    options = {
        'url': normalizeUrl(opts.url),
        'method': opts.method.lower(),
        'params': parseQuery(opts.params),
        'data': parseQuery(opts.data),
        'headers': parseQuery(opts.headers),
        'cookies': parseQuery(opts.cookies),
    }
    m = Mutator(options)
    m.fuzz(opts.part, opts.key, opts.vuln, opts.interval)
    print('Done')


if __name__ == '__main__':
    main()
