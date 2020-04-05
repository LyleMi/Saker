#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from multiprocessing import Process
from saker.servers.socket.tcp import TCPServer
from saker.core.rawhttp import RawHTTP


def startServer(addr, port):
    tcpserver = TCPServer(addr, port)
    tcpserver.handle_request()


class RawHttpTest(unittest.TestCase):

    bindip = '127.0.0.1'
    port = 7777

    def setUp(self):
        p = Process(
            target=startServer, args=(
                self.bindip, self.port
            )
        )
        p.start()

    def addCleanup(self):
        pass

    def test_send(self):
        req = ['POST /tests HTTP/1.1']
        req += ['Host: 127.0.0.1:9515']
        req += ['Content-Type: application/json']
        req += ['Content-Length: 12']
        req += ['']
        req += ['{"test": {}}']
        req = RawHTTP.split.join(req)
        resp = RawHTTP.sendBytes(self.bindip, self.port, req)
        print(resp)

    def test_construct(self):
        headers = {
            'Cookie': 'a=b;'
        }
        req = RawHTTP.construct(
            method='POST',
            url='/admin?username=admin',
            headers=headers,
            body='login=true'
        )
        resp = RawHTTP.sendBytes(self.bindip, self.port, req)
        print(req)
        print(resp)


if __name__ == '__main__':

    unittest.main()
