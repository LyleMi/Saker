import os
import qqwry

# pip install qqwry-py3


class GeoIP(object):

    def __init__(self, update=False):
        super(GeoIP, self).__init__()
        qdat = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qqwry.dat")
        if not os.path.exists(qdat) or update:
            ret = qqwry.updateQQwry(qdat)
        self.q = qqwry.QQwry()
        self.q.load_file(qdat)

    def lookup(self, ip):
        return self.q.lookup(ip)
