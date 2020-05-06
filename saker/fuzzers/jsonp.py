# https://github.com/p1g3/JSONP-Hunter

from saker.fuzzers.fuzzer import Fuzzer


class JSONP(Fuzzer):

    payloads = [
        # just replace
        'alert',
        # test `.`
        'console.log',
        'eval',
        'Function',
        'xxx',
        'xxx()',
        'xxx``',
        'xxx("")',
        """xxx(""+''+``);//%""",
        "'",
        '"',
        '\\',
        '`',
        '//',
        ';',
        '%',
    ]
