import os
import unittest

from saker.utils.serializer import Serializer


class SerializerTest(unittest.TestCase):

    def test_json(self):
        s = Serializer()
        obj = {
            "fuzz": [1]
        }
        s.save(obj, "test")
        obj_new = s.load("test")
        self.assertEqual(obj, obj_new)
        s.remove("test")


if __name__ == '__main__':
    unittest.main()
