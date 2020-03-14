#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from saker.port.nmap import Nmap
from saker.utils.daemon import Daemon


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
