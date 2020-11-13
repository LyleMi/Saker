#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from multiprocessing import Process
from saker.servers.socket.tcp import TCPServer
from saker.core.rawhttp import RawHTTP


def startServer(addr, port):
    tcpserver = TCPServer(addr, port)
    tcpserver.handle_request()

def start_server(addr, port):
    p = Process(
        target=startServer, args=(
            addr, port
        )
    )
    p.start()

class RawHttpTest(unittest.TestCase):

    bindip = "127.0.0.1"
    port = 7777

    def test_send(self):
        req = ["POST /tests HTTP/1.1"]
        req += ["Host: 127.0.0.1:9515"]
        req += ["Content-Type: application/json"]
        req += ["Content-Length: 12"]
        req += [""]
        req += ["{\"test\": {}}"]
        req = "\r\n".join(req)
        r = RawHTTP()
        resp = r.sendBytes("http://%s:%s" % (self.bindip, self.port), req)
        print(resp)

    def test_construct(self):
        headers = {
            "Cookie": "a=b;"
        }
        r = RawHTTP()
        data = r.construct(
            method="POST",
            url="/admin?username=admin",
            headers=headers,
            body="login=true"
        )
        resp = r.sendBytes("http://%s:%s" % (self.bindip, self.port), data)
        print(resp)

    def test_https(self):
        r = RawHTTP()
        data = r.construct(method="GET")
        resp = r.sendBytes("https://127.0.0.1", data)
        print(resp)


if __name__ == '__main__':
    start_server(RawHttpTest.bindip, RawHttpTest.port)
    unittest.main()
