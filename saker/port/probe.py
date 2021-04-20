#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import requests


class Probe(object):

    knownPorts = {
        21: "tcp",
        22: "ssh",
        23: "telnet",
        80: "http",
        111: "rpcbind",
        135: "smb",
        443: "https",
        2049: "nfs",
        3306: "mysql",
        3389: "rdp",
        8080: "http",
        6379: "redis",
    }

    banners = {
        "ftp": ["vsFTPd"],
        "ActiveMQ": ["ActiveMQ"],
    }

    def __init__(self, timeout=5):
        super(Probe, self).__init__()
        self.timeout = timeout

    def test(self, addr, port):
        if port in self.knownPorts:
            print("known ports, skip")
            return self.knownPorts[port]
        ret = self.http(addr, port)
        if ret is not None:
            return ret
        else:
            print("not http, continue")
        ret = self.http(addr, port)
        if ret is not None:
            return ret
        else:
            print("not https, continue")
        return self.normalTcp(addr, port)

    def http(self, addr, port):
        url = "http://%s:%s" % (addr, port)
        try:
            r = requests.get(url, timeout=self.timeout)
            print(r.content)
            return True
        except requests.exceptions.ConnectionError as e:
            return None
        except Exception as e:
            print(repr(e))
            return None

    def https(self, addr, port):
        url = "https://%s:%s" % (addr, port)
        try:
            r = requests.get(
                url,
                verify=False,
                timeout=self.timeout
            )
            print(r.content)
            return True
        except requests.exceptions.ConnectionError as e:
            return None
        except Exception as e:
            print(repr(e))
            return None

    def normalTcp(self, addr, port):
        cli = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        cli.settimeout(self.timeout)
        cli.connect((addr, port))
        cli.send(b"AAA")
        try:
            recv = cli.recv(4096)
            print(recv)
            return True
        except socket.timeout as e:
            return None
        except Exception as e:
            print(repr(e))
            return None
