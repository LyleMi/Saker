import socks
import socket


def setProxy(addr, port, username=None, password=None, proxy_type=socks.SOCKS5):
    # pip install PySocks
    socks.set_default_proxy(
        proxy_type, addr=addr, port=port,
        username=username, password=password
    )
    socket.socket = socks.socksocket
