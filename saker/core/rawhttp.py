import socket


class RawHTTP(object):

    split = '\r\n'
    template = '<method> <request-URL> <version>\r\n<headers>\r\n<entity-body>\r\n'

    def __init__(self):
        super(RawHTTP, self).__init__()

    @classmethod
    def construct(cls, method='GET', url='/', headers={}, body='', version='HTTP/1.1'):
        data = cls.template
        data = data.replace('<method>', method)
        data = data.replace('<request-URL>', url)
        data = data.replace('<version>', version)
        strHeader = ''
        if len(body) > 1:
            headers['Content-Length'] = len(body)
        for k in headers:
            strHeader += '%s: %s%s' % (k, headers[k], cls.split)
        data = data.replace('<headers>', strHeader)
        data = data.replace('<entity-body>', body)
        return data

    @classmethod
    def sendBytes(cls, addr, port, req):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr, port))
        if isinstance(req, str):
            req = req.encode()
        s.send(req)
        resp = s.recv(4096)
        s.close()
        return resp
