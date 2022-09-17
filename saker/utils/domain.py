#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import socket

from netaddr import IPRange, IPNetwork


class RES:
    ip = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    cidr = re.compile(r"\d+\.\d+\.\d+\.\d+(?:\/\d+)?$")
    v4range = re.compile(r"\d+\.\d+\.\d+\.\d+\-\d+\.\d+\.\d+\.\d+$")
    v6range = re.compile(r"[0-9a-fA-F]+:[0-9A-Fa-f:.]+\-[0-9a-fA-F]+:[0-9A-Fa-f:.]+$")
    glob = re.compile(r"\d+\.\d+\.\d+\.\*$")
    bracket = re.compile(r"(.*?)\.(\d+)[\[\{\(](.*)[\)\}\]]$")  # parses '1.2.3.4[5-9]' or '1.2.3.[57]'
    crange = re.compile(r"(.*?)\.(\d+)\-(\d+)$")
    brange = re.compile(r"(.*?)\.(\d+)\-(\d+).(\d+)$")
    hostname = re.compile(r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?)', re.IGNORECASE)


def cidrize(ipstr):
    """
    将各种格式的IP字符串扩展为IP列表

    1.1.1.1,1.1.1.2
    1.1.1.1-124
    1.1.1.1/24
    1.2.3.4[5-9]
    """
    ipstr = ipstr.replace(' ', '').strip()

    if isIPv4(ipstr):
        return [ipstr]

    ips = []
    if ',' in ipstr:
        for ip in ipstr.split(","):
            ips.extend(cidrize(ip))
        return list(set(ips))

    if RES.cidr.match(ipstr):
        return [str(i) for i in IPNetwork(ipstr)]

    if RES.v4range.match(ipstr):
        start, finish = ipstr.split('-')
        return [str(i) for i in IPRange(start, finish)]

    if RES.crange.match(ipstr):
        # c段
        start, finish = ipstr.split('-')
        finish = ".".join(start.split(".")[:-1] + [finish])
        return [str(i) for i in IPRange(start, finish)]

    if RES.brange.match(ipstr):
        # b段
        parts = ipstr.split('.')
        temp = parts[2].split("-")
        for i in range(int(temp[0]), int(temp[1]) + 1):
            parts[2] = str(i)
            ips.append(".".join(parts))
        return ips

    if RES.bracket.match(ipstr):
        match = RES.bracket.match(ipstr)
        parts = match.groups()

        if len(parts) == 3:
            prefix, subnet, enders = parts
            network = '.'.join((prefix, subnet))

        # '1.2.3.[5-9] style
        elif len(parts) == 2:
            prefix, enders = parts
            network = prefix + '.'

        # Split hyphenated [x-y]
        if '-' in enders:
            first, last = enders.split('-')

        # Get first/last from [xy] - This really only works with single
        # digits
        elif len(enders) >= 2:
            # Creating a set and sorting to ensure that [987] won't throw
            # an exception. Might be too inclusive, but screw it.
            uniques = sorted(set(enders))
            first = uniques[0]
            last = uniques[-1]

        return [str(i) for i in IPRange(network + first, network + last)]

    return ips


def isUniversalParsing(domain):
    # 判断是否为泛解析
    # 注：当一个域名解析为空的时候，也会返回True
    try:
        t1 = domain2ips(domain)
        t2 = domain2ips("this-would-not-exists." + domain)
        t3 = domain2ips("i-dont-believe-this-could-exists." + domain)
        if t1 == t2 and t1 == t3:
            return True
    except socket.gaierror as e:
        pass
    return False


def isIPv4(ip):
    # 判断是否为ipv4
    return bool(RES.ip.match(ip))


def isCDN(domain):
    # to do
    pass


def ip2domain(ip):
    domain = 'no-data'
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except socket.herror as e:
        return None
    if domain == 'no-data':
        return None
    return domain


def domain2ips(domain):
    try:
        ips = map(lambda i: i[4][0], socket.getaddrinfo(domain, None))
    except socket.gaierror as e:
        return []
    ips = filter(lambda i: i != "0.0.0.0", ips)
    ips = filter(isIPv4, ips)
    return set(ips)


def gethostip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr




def isInternal(seed, stype):

    if stype == "IP":
        return isInternalIp(seed)

    if stype == "DOMAIN" or stype == "MAIN_DOMAIN":
        ips = domain2ips(seed)
        for ip in ips:
            if isInternalIp(ip):
                return True

    if stype == "NETBLOCK":
        return isInternalIp(seed.split("/")[0])
    return False


def get_domain(domain):
    import tldextract
    r = tldextract.extract(domain)
    return "%s.%s" % (r.domain, r.suffix)
