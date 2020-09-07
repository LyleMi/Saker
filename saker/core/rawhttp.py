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
        return data.encode()

    def connect(self, url):
        url = urlparse(url)
        addr = url.netloc.split(":")[0]
        if self.socket is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = self.socket(socket.AF_INET, socket.SOCK_STREAM)
        if url.scheme == 'https':
            # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.verify_mode = ssl.CERT_NONE
            s = context.wrap_socket(
                s,
                server_side=False,
            )
            # s = context.wrap_socket(s, server_hostname=url.hostname)
            # s = context.wrap_socket(s, server_hostname="vpn.safeapp.com.cn")
        s.connect((addr, url.port))
        return s

    def sendBytes(self, url, req):
        s = self.connect(url)
        if isinstance(req, str):
            req = req.encode()
        s.send(req)
        resp = s.recv(4096)
        s.close()
        return resp
