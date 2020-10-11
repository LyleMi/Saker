from saker.servers.socket.dnsproxy import HexServer
from saker.servers.socket.dnsproxy import DNSProxyServer


def hexServer():
    dnsServer = HexServer()
    dnsServer.serve_forever()


def main():
    dnsserver = DNSProxyServer()
    dnsserver.serve_forever()


if __name__ == '__main__':
    main()
