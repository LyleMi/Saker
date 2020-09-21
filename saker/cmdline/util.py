import argparse

from saker.utils.geoip import GeoIP


def util(args):
    parser = argparse.ArgumentParser(
        description='Saker Command Line Utils',
        usage='[options]',
        epilog='Saker Command Line Utils'
    )
    parser.add_argument(
        '-t', '--tool', metavar='tool',
        default='',
        help='tool name'
    )
    parser.add_argument(
        '-p', '--params', metavar='params',
        default='',
        help='tool params'
    )
    opts = parser.parse_args(args)

    if opts.tool == "geo":
        g = GeoIP()
        info = g.lookup(opts.params)
        print(info)
