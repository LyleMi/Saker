import unittest

from saker.utils.geoip import GeoIP
from saker.utils.geoip import GeoLite


class GeoTest(unittest.TestCase):

    def test_look(self):
        g = GeoIP()
        self.assertEqual(g.lookup("8.8.8.8")[0], "美国")
        self.assertEqual(g.lookup("1.1.1.1")[0], "美国")

    def test_city(self):
        g = GeoLite()
        self.assertEqual(g.city("8.8.8.8"), "")

    def test_city_name(self):
        g = GeoLite()
        self.assertEqual(g.city_name("8.8.8.8"), "")
        self.assertEqual(g.city_name("106.11.172.56"), "")


if __name__ == '__main__':
    unittest.main()
