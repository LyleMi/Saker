import ssl
import socket

from saker.brute.brute import Brute


class CobaltStrike(Brute):

    def __init__(self):
        super(CobaltStrike, self).__init__()
        self.sock = None
        self.ssl_sock = None
        self.ctx = ssl.SSLContext()
        self.ctx.verify_mode = ssl.CERT_NONE
        self.timeout = 10

    def is_connected(self):
        return self.sock and self.ssl_sock

    def open(self, addr, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.ssl_sock = self.ctx.wrap_socket(self.sock)

        if addr == socket.gethostname():
            ip = socket.gethostbyname_ex(addr)[2][0]
            self.ssl_sock.connect((ip, port))
        else:
            self.ssl_sock.connect((addr, port))

    def send(self, buf):
        if not self.ssl_sock:
            raise Exception("Not connected")
        self.ssl_sock.sendall(buf)

    def receive(self):
        if not self.ssl_sock:
            raise Exception("Not connected")
        received_size = 0
        data_buffer = b""

        while received_size < 4:
            data_in = self.ssl_sock.recv()
            data_buffer = data_buffer + data_in
            received_size += len(data_in)
        return data_buffer

    def close(self):
        if self.sock:
            self.sock.close()
        self.sock = None
        self.ssl_sock = None

    def buildPayload(password):
        payload = b"\x00\x00\xbe\xef"
        payload += len(password).to_bytes(1, "big", signed=True)
        payload += bytes(password, "ascii").ljust(256, b"A")
        return payload

    def run(self, addr, port, password):
        self.open(addr, port)
        self.send(self.buildPayload(payload))
        result = self.receive()
        return result == b"\x00\x00\xca\xfe"
