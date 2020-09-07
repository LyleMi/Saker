import socket

class Sock(object):

    def __init__(self, addr, port):
        super(Sock, self).__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send(self, data):
        return self.client.send(data)

    def recv(self, len=None):
        return self.client.recv(len)
