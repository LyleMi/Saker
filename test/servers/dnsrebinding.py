from saker.servers.socket.dnsrebinding import RebindingServer


def main():
    values = {
        'result': ['8.8.8.8', '127.0.0.1'],
        'index': 0
    }
    dnsServer = RebindingServer(values)
    dnsServer.serve_forever()


if __name__ == '__main__':
    main()
