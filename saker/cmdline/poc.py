#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import importlib



def poc(args):
    parser = argparse.ArgumentParser(
        description="Saker PoC Runner",
        usage="[options]",
        epilog="run PoC"
    )
    parser.add_argument(
        "-u", "--url",
        dest="url", help="define specific url"
    )
    parser.add_argument(
        "-l", "--list",
        dest="targetlist", help="use file as poc target"
    )
    parser.add_argument(
        "-f", "--file",
        dest="file", help="read poc file"
    )
    parser.add_argument(
        "-n", "--name",
        dest="name", help="poc class name, default use file"
    )
    parser.add_argument(
        "-p", '--proxy',
        dest="proxy", help="proxy url"
    )
    opts = parser.parse_args(args)

    url = opts.url
    targetlist = opts.targetlist
    file = opts.file

    if not file or ((not url) and (not targetlist)):
        parser.print_help()
        return

    if file.endswith(".py"):
        file = file[:-3]
    poc = importlib.import_module(file)
    if not opts.name:
        name = file.split(".")[-1].capitalize()
    else:
        name = opts.name
    poc_class = getattr(poc, name)
    poc = poc_class()

    if opts.proxy:
        poc.setProxies(opts.proxy)

    if targetlist:
        with open(targetlist, "r", encoding="utf-8") as fp:
            content = fp.read()
            lines = content.split("\n")
            for line in lines:
                if line == "":
                    continue
                poc.verify(line)
    if url:
        poc.verify(url)
