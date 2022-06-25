import argparse

from saker.utils.geoip import GeoIP
from saker.utils.geoip import GeoLite
from saker.utils.encode import decodeURL
from saker.utils.encode import b64d
from saker.utils.encode import unhex

def util(args):
    parser = argparse.ArgumentParser(
        description="Saker Command Line Utils",
        usage="[options]",
        epilog="Saker Command Line Utils"
    )
    parser.add_argument(
        "-t", "--tool", metavar="tool",
        default="",
        help="tool name, support geo/unhex/b64d/urld now"
    )
    parser.add_argument(
        "-p", "--params", metavar="params",
        default="",
        help="tool params"
    )
    # opts = parser.parse_args(args)
    opts, remains = parser.parse_known_args()
    remains = remains[1:]

    if opts.tool == "geo":
        g = GeoIP()
        info = g.lookup(opts.params)
        print(info)
    elif opts.tool == "geofile":
        g = GeoIP()
        glite = GeoLite()
        with open(opts.params, "r", encoding="utf-8") as fp:
            for line in fp:
                ip = line.strip()
                info = g.lookup(ip)
                city_name = glite.city_name(ip)
                print(ip, info, city_name)
    elif opts.tool == "unhex":
        print(unhex(remains[0]))
    elif opts.tool == "b64d":
        print(b64d(remains[0]))
    elif opts.tool == "urld":
        print(decodeURL(remains[0]))
