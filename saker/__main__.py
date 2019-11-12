#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from pprint import pprint

from saker.data.banner import banner
from saker.core.scaner import Scanner
from saker.core.mutator import Mutator
from saker.core.request import Request
from saker.port.nmap import Nmap
from saker.utils.url import parseQuery
from saker.utils.url import normalizeUrl
from saker.utils.daemon import Daemon


def main():
    if sys.argv[1] == 'scan':
        scanner(sys.argv[2:])
    elif sys.argv[1] == 'fuzz':
        fuzz(sys.argv[2:])
    elif sys.argv[1] == 'port':
        port(sys.argv[2:])
    else:
        print('unknown command')


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

    print(banner)

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


def port(args):
    parser = argparse.ArgumentParser(
        description='Saker Port Scanner',
        usage='[options]',
        epilog='Nmap wrapper'
    )
    parser.add_argument(
        "-t", '--target',
        dest="target", help="define scan target"
    )
    parser.add_argument(
        "-f", '--file',
        dest="file", help="use file as scan target"
    )
    parser.add_argument(
        '-b', '--background', action="store_true",
        help='run port scanner in background with unix daemon, only support unix platform'
    )
    opts = parser.parse_args(args)

    targets = []
    task = ''

    if opts.file:
        task = opts.file
        with open(opts.file, 'r') as fh:
            for domain in fh:
                targets.append(domain.strip())

    if opts.target:
        task = opts.target
        target.append(opts.target)

    if len(targets) < 1:
        parser.print_help()
        return

    def _nmapScan(target):
        for target in targets:
            Nmap(target).dump()

    if opts.background:
        pidfile = '%s.pid' % task
        logfile = '%s.log' % task
        errfile = '%s.err' % task
        d = Daemon(pidfile, stdout=logfile, stderr=errfile)
        d.start(_nmapScan, targets)
    else:
        _nmapScan(targets)


if __name__ == '__main__':
    main()
