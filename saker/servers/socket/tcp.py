import socketserver


class CustomTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data)


class TCPServer(socketserver.TCPServer):

    def __init__(self, host, port, handler=CustomTCPHandler):
        super(TCPServer, self).__init__(
            (host, port), handler
        )
