from saker.servers.socket.tcp import TCPServer


def main():
    tcpserver = TCPServer('127.0.0.1', 7777)
    tcpserver.serve_forever()


if __name__ == '__main__':
    main()
