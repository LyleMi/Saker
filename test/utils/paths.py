import os
import unittest

from saker.utils.paths import Paths
from saker.utils.paths import traverse
from saker.utils.paths import getUpper


class DirTest(unittest.TestCase):

    def test_paths(self):
        print(Paths.base)

    def test_traverse(self):
        base = getUpper(getUpper(os.path.abspath(__file__)))
        for filepath, filename in traverse(base):
            print(filepath, filename)
        for filepath, filename in traverse(base, True):
            print(filepath, filename)


if __name__ == '__main__':
    unittest.main()
