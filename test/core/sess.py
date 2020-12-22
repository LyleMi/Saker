import unittest
from saker.core.sess import Sess


class SessTest(unittest.TestCase):

    def test_ua(self):
        s = Sess()
        s.setUA()


if __name__ == '__main__':
    unittest.main()
