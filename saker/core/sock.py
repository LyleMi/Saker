import socket


class SockType:

    TCP = 1
    UDP = 0


class Sock(object):

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

    def setTimeout(self, timeout=None):
        self.sock.settimeout(timeout)

    def close(self):
        self.sock.close()


class tcpSock(Sock):

    def __init__(self, addr, port):
        super(tcpSock, self).__init__(addr, port)
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        self.sock.connect((addr, port))

    def send(self, data):
        return self.sock.send(data)

    def recv(self, len=None):
        return self.sock.recv(len)


class udpSock(Sock):

    def __init__(self, addr, port):
        super(udpSock, self).__init__(addr, port)
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM
        )

    def send(self, data):
        return self.sock.sendto(data, (self.addr, self.port))

    def recv(self, len=4096):
        return self.sock.recvfrom(len)


def autoSock(addr, port, type):
    if type == "tcp":
        sock = tcpSock(addr, port)
    else:
        sock = udpSock(addr, port)
    return sock
