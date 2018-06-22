#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket


class memcachedDetect(object):

    def __init__(self):
        super(memcachedDetect, self).__init__()
        self.name = "memcachedDetect"

    def run(self, ip, port=11211):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send('stats\r\n')
            if 'version' in s.recv(1024):
                s.close()
                return True
        except TimeoutError as e:
            return False


if __name__ == '__main__':
    pass
