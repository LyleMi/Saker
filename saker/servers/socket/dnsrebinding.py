#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import time
import dnslib
import socketserver


class DNSServer(socketserver.UDPServer):

    def __init__(self, options):
        socketserver.UDPServer.__init__(
            self, ('0.0.0.0', 53), RequestHandler
        )
        self.result = options['result']
        self.resultIdx = 0
        self.ttl = options['ttl']
        self.recordType = options['recordType']

    def getRecord(self):
        record = self.result[self.resultIdx % len(self.result)]
        self.resultIdx += 1
        return record


class RequestHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        ttl = self.server.ttl
        recordType = self.server.recordType

        request = dnslib.DNSRecord.parse(self.packet).reply()
        qname = request.q.qname.__str__()
        record = self.server.getRecord()

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
    options = {
        'ttl': 0,
        'recordType': 'A',
        'result': ['8.8.8.8', '127.0.0.1']
    }
    dnsServer = DNSServer(options)
    dnsServer.serve_forever()


if __name__ == '__main__':
    main()
