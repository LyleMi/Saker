#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


class telnetDetect(object):

    def __init__(self):
        super(telnetDetect, self).__init__()
        self.name = "telnetDetect"

    def run(self, ip, port=23):
        try:
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024)
            if banner.endswith('login: '):
                banner = banner[:-7]
            self.banner = repr(banner)
        except Exception as e:
            return False
        finally:
            s.close()
            self.clear()

        return True


if __name__ == '__main__':
    telnetTest = telnetDetect("0.0.0.0")
