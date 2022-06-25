import socket
import struct


def ip2int(addr):
    # https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))
