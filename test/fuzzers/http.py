import random
import unittest

from saker.fuzzers.http import HTTPFuzzer


class HTTPFuzzerTest(unittest.TestCase):

    def test_verb(self):
        random.seed(0)
        targets = ["POST", "SET", "OPTIONS", "POST", "INFO"]
        for i in range(5):
            self.assertEqual(HTTPFuzzer.verb(), targets[i])

    def test_version(self):
        targets = ["HTTP/0.9", "HTTP/1.0", "HTTP/0.9"]
        for i in range(3):
            self.assertEqual(HTTPFuzzer.version(), targets[i])


if __name__ == '__main__':
    unittest.main()
