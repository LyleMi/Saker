#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import struct
from io import BytesIO
from paramiko import Transport

# refer:
# https://stribika.github.io/2015/01/04/secure-secure-shell.html
# http://blog.csdn.net/macrossdzh/article/details/5691924
# http://www.iodigitalsec.com/ssh-fingerprint-and-hostkey-with-paramiko-in-python/
# RFC-4251~4


class SSH(object):

    def __init__(self):
        super(SSH, self).__init__()
        self.data = {}

    def run(self, ip, port=22, timeout=2):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(50).strip(b"\r\n").split(b" ")
            try:
                self.data["version"] = banner[0].decode()
                self.data["os"] = banner[1].decode()
            except IndexError:
                pass

            s.send(banner[0] + b"\r\n")
            self._raw_recv = s.recv(2048)

            s.close()
            self._parse_raw_data()

            tran = Transport((ip, port))
            tran.start_client()
            pubkey = tran.get_remote_server_key()
            self.data["pubkey_name"] = pubkey.get_name()
            fp = pubkey.get_fingerprint()
            self.data["pubkey_fingerprint"] = fp.hex()
        except Exception as e:
            print(repr(e))
            return None
        finally:
            tran.close()
        return True

    def _parse_raw_data(self):
        stream = BytesIO(self._raw_recv)
        packet_length = struct.unpack(">i", stream.read(4))[0]
        padding_length = ord(stream.read(1))
        message_code = ord(stream.read(1))
        cookie = stream.read(16)
        keys = [
            "kex_algo",
            "server_host_key_algo",
            "enc_algo_client_to_server",
            "enc_algo_server_to_client",
            "mac_algo_client_to_server",
            "mac_algo_server_to_client",
            "compress_algo_client_to_server",
            "compress_algo_server_to_client",
            "lang_client_to_server",
            "lang_server_to_client",
        ]
        for key in keys:
            length = struct.unpack(">i", stream.read(4))[0]
            data = stream.read(length)
            self.data[key] = data.decode().split(",")
