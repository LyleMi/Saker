import random
import socket
import socketserver

import dnslib

from saker.core.sock import udpSock
from saker.utils.logger import getLogger


class DNSProxyServer(socketserver.UDPServer):

    def __init__(self, addr="0.0.0.0", port=53, uplists=[]):
        socketserver.UDPServer.__init__(
            self, (addr, port), RequestHandler
        )
        if len(uplists) < 1:
            uplists = [
                "1.1.1.1",
                "8.8.4.4",
                "8.8.8.8",
                "114.114.114.114",
                "114.114.115.115",
                "223.5.5.5",
                "223.6.6.6",
            ]
        self.uplists = uplists
        self.logger = getLogger()
        self.logger.debug("start dns proxy server")
        # for upstream dns server not response
        self.retry = 3

    def getRecord(self, packet):
        try:
            for _ in range(self.retry):
                resp = self.getFromUpSrv(packet)
                return resp
        except socket.timeout as e:
            self.logger.debug("upstream timeout")
        return b""

    def getFromUpSrv(self, packet):
        upSrv = random.choice(self.uplists)
        u = udpSock(upSrv, 53)
        u.setTimeout(3)
        self.logger.debug("forward %s data to %s" % (len(packet), upSrv))
        u.send(packet)
        resp = u.recv()
        u.close()
        return resp[0]


class RequestHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        resp = self.server.getRecord(self.packet)
        request = dnslib.DNSRecord.parse(self.packet).reply()
        qname = str(request.q.qname)
        qclass = str(request.q.qclass)
        qtype = str(request.q.qtype)
        zone = request.q.toZone()
        # print(dir(request.q))
        self.server.logger.debug("%s query %s" % (self.client_address, zone))
        self.wfile.write(resp)
