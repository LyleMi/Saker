import re
import argparse

def file(args):
    parser = argparse.ArgumentParser(
        description="Saker Command line file process",
        usage="[options]",
        epilog="Saker Command line file process"
    )
    parser.add_argument(
        "-i", "--input",
        default="input.txt", dest="input",
        help="inputfile"
    )
    parser.add_argument(
        "-o", "--output",
        default="output.txt", dest="output",
        help="inputfile"
    )
    parser.add_argument(
        "-t", "--type",
        default="filter", dest="type",
        help="process type"
    )
    parser.add_argument(
        "-e", "--expression",
        default="*", dest="expression",
        help="process expression"
    )
    opts = parser.parse_args(args)
    with open(opts.input, "r", encoding="utf-8") as fp:
        content = fp.read()
    if opts.type in ["e", "extract"]:
        regexp = re.compile(opts.e)
        extract = re.findall(regexp, content)
        extract = list(set(extract))
        extract.sort()
        output = "\n".join(extract)
    with open(opts.output, "w", encoding="utf-8") as fp:
        fp.write(output)
