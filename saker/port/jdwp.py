#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import sys


from saker.utils.binutils import p32, u32


class jdwpDetect(object):

    def __init__(self):
        super(jdwpDetect, self).__init__()
        self.name = "jdwpDetect"

    def run(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        handshake = 'JDWP-Handshake'
        s.send(handshake)
        data = s.recv(len(handshake))
        print(data)
        if data != handshake:
            return False
        versionCommandPack = p32(1)
        versionCommandPack += b'\x00\x01\x01'
        versionCommandPack = p32(len(versionCommandPack) + 4) + versionCommandPack
        s.send(versionCommandPack)
        data = s.recv(4)
        replyLength = u32(data)
        print("get reply size: {}".format(replyLength))
        data = s.recv(replyLength)
        print(data)
        s.close()
        return True


if __name__ == '__main__':
    check(sys.argv[1], sys.argv[2])
