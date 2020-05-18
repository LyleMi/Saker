#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import time
import dnslib
import socketserver


class RebindingServer(socketserver.UDPServer):

    def __init__(self, values={}, callback=None):
        socketserver.UDPServer.__init__(
            self, ('0.0.0.0', 53), RequestHandler
        )
        if callback is None:
            self.getRecord = self._getRecord
        else:
            self.getRecord = callback
        self.values = values

    def _getRecord(self, qname):
        record = self.values['result'][self.values['index'] % len(self.values['result'])]
        self.values['index'] += 1
        ttl = 0
        recordType = 'A'
        return record, ttl, recordType


class HexServer(socketserver.UDPServer):

    def __init__(self):
        socketserver.UDPServer.__init__(
            self, ('0.0.0.0', 53), RequestHandler
        )

    def getRecord(self, qname):
        payload = qname.split('.')[0]
        try:
            record = bytes.fromhex(payload).decode()
        except Exception as e:
            record = '127.0.0.1'
        ttl = 600
        recordType = 'A'
        return record, ttl, recordType


class RequestHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        request = dnslib.DNSRecord.parse(self.packet).reply()
        qname = str(request.q.qname)
        record, ttl, recordType = self.server.getRecord(qname)
        answer = dnslib.DNSRecord.question(qname)
        request.add_answer(
            dnslib.RR(
                qname,
                getattr(dnslib.QTYPE, recordType),
                rdata=getattr(dnslib, recordType)(record),
                ttl=ttl
            )
        )
        print('[%s] %s %s %s' % (time.time(), self.client_address, qname, record))
        self.wfile.write(request.pack())


def main():
    hexServer()


def rebindingServer():
    values = {
        'result': ['8.8.8.8', '127.0.0.1'],
        'index': 0
    }
    dnsServer = RebindingServer(values)
    dnsServer.serve_forever()


def hexServer():
    dnsServer = HexServer()
    dnsServer.serve_forever()


if __name__ == '__main__':
    main()
