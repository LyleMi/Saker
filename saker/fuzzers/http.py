#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer

_status_code = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    305: 'Switch Proxy',
    307: 'Temporary Redirect',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request-URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    421: 'Too Many Connections',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    425: 'Unordered Collection',
    426: 'Upgrade Required',
    449: 'Retry With',
    451: 'Unavailable For Legal Reasons',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    509: 'Bandwidth Limit Exceeded',
    510: 'Not Extended',
    600: 'Unparseable Response Headers',
}

_verbs = [
    'SET',
    'REMOVE',
    'DEBUG',
    'TRACK',
    'CONNECT',
    'TRACE',
    'FORWARD',
    'INFO',
    'OPTIONS',
    'HEAD',
    'GET',
    'PUT',
    'POST',
    'DELETE',
]

_versions = [
    "HTTP/0.9",
    "HTTP/1.0",
    "HTTP/1.1",
]


class HTTPFuzzer(Fuzzer):

    '''HTTPFuzzer'''

    status_code = _status_code
    verbs = _verbs
    versions = _versions

    def __init__(self):
        super(HTTPFuzzer, self).__init__()

    def trace(self):
        '''
        trace method test
        '''
        pass

    def put(self):
        '''
        put method test
        '''
        pass

    def illegal(self, method='ILLEGAL'):
        '''
        illegal method test
        '''
        pass

    def raw(self):
        '''
        raw HTTP connection
        '''
        pass

    @classmethod
    def verb(cls, pro=0.95):
        if cls.r.random() > pro:
            return cls.randomStr()
        else:
            return cls.choice(cls.verbs)

    @classmethod
    def version(cls, pro=0.99):
        if cls.r.random() > pro:
            return cls.randomStr()
        else:
            return cls.choice(cls.versions)
