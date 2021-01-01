import unittest
from saker.port.ssh import SSH

class SSHTest(unittest.TestCase):

    def test_scan(self):
        o = SSH()
        o.run("127.0.0.1")
        print(o.data)

if __name__ == '__main__':
    unittest.main()
