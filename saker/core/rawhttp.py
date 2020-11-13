from urllib.parse import urlparse

from saker.core.sock import tcpSock


class RawHTTP(object):

    split = '\r\n'
    template = '<method> <request-URL> <version>\r\n<headers>\r\n<entity-body>\r\n'

    def __init__(self):
        super(RawHTTP, self).__init__()

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
        port = url.port
        if port is None:
            port = [80, 443][url.scheme == "https"]
        conn = tcpSock(addr, port, url.scheme == "https")
        return conn

    def sendBytes(self, url, req):
        s = self.connect(url)
        if isinstance(req, str):
            req = req.encode()
        s.send(req)
        resp = s.recv(4096)
        s.close()
        return resp
