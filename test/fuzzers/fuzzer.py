import random
import unittest

from saker.fuzzers.fuzzer import Fuzzer


class FuzzerTest(unittest.TestCase):

    def test_randomStr(self):
        random.seed(0)
        self.assertEqual(Fuzzer.randomStr(length=10), "N\rR5x$!PCZ")

    def test_weightRandom(self):
        random.seed(0)
        picks = [Fuzzer.weightRandom([5, 2, 1, 1]) for i in range(20)]
        self.assertEqual(picks, [1, 1, 0, 0, 3, 2, 1, 0, 2, 1, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0])


if __name__ == '__main__':
    unittest.main()
