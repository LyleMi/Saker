from saker.servers.socket.tcp import TCPServer

if __name__ == '__main__':
    tcpserver = TCPServer('127.0.0.1', 7777)
    tcpserver.serve_forever()
