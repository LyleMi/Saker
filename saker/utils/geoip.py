import os
import qqwry
import geoip2.errors
import geoip2.database

# pip install qqwry-py3
# pip install geoip2


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


class GeoLite(object):

    def __init__(self):
        mmdb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GeoLite2-City.mmdb")
        self.reader = geoip2.database.Reader(mmdb)

    def city(self, ip):
        try:
            return self.reader.city(ip)
        except geoip2.errors.AddressNotFoundError as e:
            return None

    def city_name(self, ip, lang="zh-CN"):
        city_info = self.city(ip)
        if not city_info.city.names:
            return ""
        else:
            return city_info.city.names.get(lang, "")
