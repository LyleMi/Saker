#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from saker.core.mutator import Mutator
from saker.core.request import Request

from saker.utils.url import parseQuery
from saker.utils.url import normalizeUrl


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
