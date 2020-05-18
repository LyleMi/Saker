import ssl
import socket

from urllib.parse import urlparse


class RawHTTP(object):

    split = '\r\n'
    template = '<method> <request-URL> <version>\r\n<headers>\r\n<entity-body>\r\n'

    def __init__(self):
        super(RawHTTP, self).__init__()
        self.socket = None

    def construct(self, method='GET', url='/', headers={}, body='', version='HTTP/1.1'):
        data = self.template
        data = data.replace('<method>', method)
        data = data.replace('<request-URL>', url)
        data = data.replace('<version>', version)
        strHeader = ''
        if len(body) > 1:
            headers['Content-Length'] = len(body)
        for k in headers:
            strHeader += '%s: %s%s' % (k, headers[k], self.split)
        data = data.replace('<headers>', strHeader)
        data = data.replace('<entity-body>', body)
        return data

    def sendBytes(self, url, req):
        url = urlparse(url)
        if self.socket is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = self.socket(socket.AF_INET, socket.SOCK_STREAM)
        if url.scheme == 'https':
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            context.verify_mode = ssl.CERT_NONE
            s = context.wrap_socket(s, server_hostname=url.hostname)
        s.connect((addr, url.port))
        if isinstance(req, str):
            req = req.encode()
        s.send(req)
        resp = s.recv(4096)
        s.close()
        return resp

    def setProxy(self, addr, port, username=None, password=None, proxy_type=socks.SOCKS5):
        # pip install PySocks
        import socks
        socks.set_default_proxy(
            proxy_type, addr=addr, port=port, username=username, password=password
        )
        # socket.socket = socks.socksocket
        self.socket = socks.socksocket
