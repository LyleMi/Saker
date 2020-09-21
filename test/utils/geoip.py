import unittest

from saker.utils.geoip import GeoIP


class GeoTest(unittest.TestCase):

    def test_look(self):
        g = GeoIP()
        print(g.lookup("8.8.8.8"))


if __name__ == '__main__':
    unittest.main()
