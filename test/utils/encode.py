import unittest
from saker.utils.encode import *


class EncodeTest(unittest.TestCase):

    def test_b64e(self):
        self.assertEqual(b64e("test"), "dGVzdA==")
        self.assertEqual(b64e(b"\x01\x02\x33\x41\x00\x87\xff\x7f\x90"), "AQIzQQCH/3+Q")

    def test_b64d(self):
        self.assertEqual(b64d("dGVzdA=="), b"test")
        self.assertEqual(b64d("dGVzdA"), b"test")
        self.assertEqual(b64d("AQIzQQCH/3+Q"), b"\x01\x02\x33\x41\x00\x87\xff\x7f\x90")
        self.assertEqual(b64d("AQIzQQCH_3-Q"), b"\x01\x02\x33\x41\x00\x87\xff\x7f\x90")

    def test_hex(self):
        self.assertEqual(hex("test"), "74657374")

    def test_unhex(self):
        self.assertEqual(unhex("74657374"), "test")


if __name__ == '__main__':
    unittest.main()
