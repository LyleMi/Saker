import ssl
import socket

try:
    import socks
except Exception as e:
    print("PySocks not installed")


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

    def __init__(self, addr, port, ssl=False):
        super(tcpSock, self).__init__(addr, port)
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        if ssl:
            self.sock = wrapSSL(self.sock)
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
    elif type == "udp":
        sock = udpSock(addr, port)
    return sock


def wrapSSL(conn):
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_NONE
    conn = context.wrap_socket(
        conn,
        server_side=False,
    )
    # conn = context.wrap_socket(conn, server_hostname=url.hostname)
    # conn = context.wrap_socket(conn, server_hostname="vpn.safeapp.com.cn")
    return conn


def setProxy(addr, port, username=None, password=None, proxy_type=socks.SOCKS5):
    # pip install PySocks
    socks.set_default_proxy(
        proxy_type, addr=addr, port=port,
        username=username, password=password
    )
    socket.socket = socks.socksocket
