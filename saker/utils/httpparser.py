import socket
import struct
from urllib import parse as urlparse
from saker.utils.url import parseQuery


CRLF = '\r\n'
COLON = ':'
SP = ' '

HTTP_REQUEST_PARSER = 1
HTTP_RESPONSE_PARSER = 2

HTTP_PARSER_STATE_INITIALIZED = 1
HTTP_PARSER_STATE_LINE_RCVD = 2
HTTP_PARSER_STATE_RCVING_HEADERS = 3
HTTP_PARSER_STATE_HEADERS_COMPLETE = 4
HTTP_PARSER_STATE_RCVING_BODY = 5
HTTP_PARSER_STATE_COMPLETE = 6

CHUNK_PARSER_STATE_WAITING_FOR_SIZE = 1
CHUNK_PARSER_STATE_WAITING_FOR_DATA = 2
CHUNK_PARSER_STATE_COMPLETE = 3


class ChunkParser(object):

    """HTTP chunked encoding response parser.
    """

    def __init__(self):
        self.state = CHUNK_PARSER_STATE_WAITING_FOR_SIZE
        self.body = ''
        self.chunk = ''
        self.size = None

    def parse(self, data):
        more = True if len(data) > 0 else False
        while more:
            more, data = self.process(data)

    def process(self, data):
        if self.state == CHUNK_PARSER_STATE_WAITING_FOR_SIZE:
            line, data = HttpParser.split(data)
            self.size = int(line, 16)
            self.state = CHUNK_PARSER_STATE_WAITING_FOR_DATA
        elif self.state == CHUNK_PARSER_STATE_WAITING_FOR_DATA:
            remaining = self.size - len(self.chunk)
            self.chunk += data[:remaining]
            data = data[remaining:]
            if len(self.chunk) == self.size:
                data = data[len(CRLF):]
                self.body += self.chunk
                if self.size == 0:
                    self.state = CHUNK_PARSER_STATE_COMPLETE
                else:
                    self.state = CHUNK_PARSER_STATE_WAITING_FOR_SIZE
                self.chunk = ''
                self.size = None
        return len(data) > 0, data


class HTTP(object):

    """HTTP request/response parser.
    """

    def __init__(self, ptype=None):
        self.refresh(ptype)

    def refresh(self, ptype=None):
        self.state = HTTP_PARSER_STATE_INITIALIZED
        self.type = ptype if ptype else HTTP_REQUEST_PARSER

        self.raw = ''
        self.buffer = ''

        self.headers = dict()
        self.body = None

        self.method = None
        self.url = None
        self.code = None
        self.reason = None
        self.version = None

        self.chunker = None

    def parse(self, data):
        if data.startswith("HTTP"):
            self.type = HTTP_RESPONSE_PARSER

        self.raw += data
        data = self.buffer + data
        self.buffer = ''

        more = True if len(data) > 0 else False
        while more:
            more, data = self.process(data)
        self.buffer = data

    def process(self, data):
        if self.state >= HTTP_PARSER_STATE_HEADERS_COMPLETE and \
                (self.method == "POST" or self.type == HTTP_RESPONSE_PARSER):
            if not self.body:
                self.body = ''

            if 'content-length' in self.headers:
                self.state = HTTP_PARSER_STATE_RCVING_BODY
                self.body += data
                if len(self.body) >= int(self.headers['content-length'][1]):
                    self.state = HTTP_PARSER_STATE_COMPLETE
            elif 'transfer-encoding' in self.headers and \
                    self.headers['transfer-encoding'][1].lower() == 'chunked':
                if not self.chunker:
                    self.chunker = ChunkParser()
                self.chunker.parse(data)
                if self.chunker.state == CHUNK_PARSER_STATE_COMPLETE:
                    self.body = self.chunker.body
                    self.state = HTTP_PARSER_STATE_COMPLETE

            return False, ''

        line, data = self.split(data)
        # print line, data
        if line == False:
            return line, data

        if self.state < HTTP_PARSER_STATE_LINE_RCVD:
            self.process_line(line)
        elif self.state < HTTP_PARSER_STATE_HEADERS_COMPLETE:
            self.process_header(line)

        if self.state == HTTP_PARSER_STATE_HEADERS_COMPLETE and \
                self.type == HTTP_REQUEST_PARSER and \
                not self.method == "POST" and \
                self.raw.endswith(CRLF * 2):
            self.state = HTTP_PARSER_STATE_COMPLETE

        return len(data) > 0, data

    def process_line(self, data):
        line = data.split(SP)
        if self.type == HTTP_REQUEST_PARSER:
            self.method = line[0].upper()
            self.url = urlparse.urlsplit(line[1])
            self.version = line[2]
        else:
            self.version = line[0]
            self.code = line[1]
            self.reason = ' '.join(line[2:])
        self.state = HTTP_PARSER_STATE_LINE_RCVD

    def process_header(self, data):
        if len(data) == 0:
            if self.state == HTTP_PARSER_STATE_RCVING_HEADERS:
                self.state = HTTP_PARSER_STATE_HEADERS_COMPLETE
            elif self.state == HTTP_PARSER_STATE_LINE_RCVD:
                self.state = HTTP_PARSER_STATE_RCVING_HEADERS
        else:
            self.state = HTTP_PARSER_STATE_RCVING_HEADERS
            parts = data.split(COLON)
            key = parts[0].strip()
            value = COLON.join(parts[1:]).strip()
            self.headers[key.lower()] = (key, value)

    def build_url(self):
        if not self.url:
            return '/None'

        url = self.url.path
        if url == '':
            url = '/'
        if not self.url.query == '':
            url += '?' + self.url.query
        if not self.url.fragment == '':
            url += '#' + self.url.fragment
        return url

    def build_header(self, k, v):
        return k + ": " + v + CRLF

    def build_all_header(self):
        req = ""
        for k in self.headers:
            req += self.build_header(
                self.headers[k][0], self.headers[k][1]
            )
        return req

    def build(self, del_headers=None, add_headers=None):
        req = " ".join([self.method, self.build_url(), self.version])
        req += CRLF

        if not del_headers:
            del_headers = []
        for k in self.headers:
            if not k in del_headers:
                req += self.build_header(self.headers[k][0], self.headers[k][1])

        if not add_headers:
            add_headers = []
        for k in add_headers:
            req += self.build_header(k[0], k[1])

        req += CRLF
        if self.body:
            req += self.body
        return req

    def dictheaders(self):
        tmp = {}
        for k in self.headers:
            tmp[self.headers[k][0]] = self.headers[k][1]
        return tmp

    def dictcookies(self):
        if 'cookie' not in self.headers:
            return {}
        tmp = {}
        cookie = self.headers['cookie'][1]
        cookie = cookie.split('; ')
        for c in cookie:
            tmp[c.split('=')[0]] = c.split('=')[1]
        return tmp

    def json(self):
        return {
            "url": self.build_url(),
            "params": parseQuery(self.url.query) if self.url is not None else {},
            "data": parseQuery(self.body),
            "method": self.method,
            "version": self.version,
            "headers": self.dictheaders(),
            "cookies": self.dictcookies()
        }

    @staticmethod
    def split(data):
        pos = data.find(CRLF)
        if pos == -1:
            return False, data
        line = data[:pos]
        data = data[pos + len(CRLF):]
        return line, data


def parseHTTP(request):
    h = HTTP()
    h.parse(request)
    return h


if __name__ == '__main__':
    h = HTTP()
    h.parse('GET /')
