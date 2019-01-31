#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import sys
    import argparse

    from saker.data.banner import banner
    from saker.core.scaner import Saker

    parser = argparse.ArgumentParser(
        description='Tool For Fuzz Web Applications',
        usage='[options]',
        epilog='Tool For Fuzz Web Applications')
    parser.add_argument('-s', '--scan', action="store_true",
                        help='run with list model')
    parser.add_argument('-f', '--file', metavar='file',
                        default='',
                        help='scan specific file')
    parser.add_argument('-e', '--ext', metavar='ext',
                        default='php',
                        help='scan specific ext')
    parser.add_argument('-i', '--interactive', action="store_true",
                        help='run with interactive model')
    parser.add_argument("-u", '--url',
                        dest="url", help="define specific url")
    parser.add_argument("-p", '--proxy',
                        dest="proxy", help="proxy url")
    parser.add_argument("-t", '--timeinterval', type=float,
                        dest="interval",
                        help="scan time interval, random sleep by default",
                        default=-1)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        parser.print_help()
        sys.exit(1)

    print(banner)

    c = Saker(url)

    if opts.proxy:
        c.setProxies(opts.proxy)

    if opts.scan or opts.file:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext,
               scan=opts.scan)

    if opts.interactive:
        c.interactive()

if __name__ == '__main__':
    main()

