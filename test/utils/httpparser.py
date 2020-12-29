import unittest

from saker.utils.httpparser import HTTP


class HTTPParserTest(unittest.TestCase):

    def test_request(self):
        data = """POST /action.php?action=login&code=2 HTTP/1.1
Host: web.test.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Type: application/x-www-form-urlencoded
Content-Length: 19
Origin: http://web.test.com
Connection: close
Referer: http://web.test.com/action.php?action=login
Cookie: csrftoken=37a35c64931a61e2fb4051035a94f7ff
Upgrade-Insecure-Requests: 1

username=1&pass=223
"""
        data = data.replace("\n", "\r\n")
        http = HTTP()
        http.parse(data)
        self.assertEqual(http.method, "POST")
        self.assertEqual(http.url.path, "/action.php")
        self.assertEqual(http.version, "HTTP/1.1")
        self.assertEqual(http.build_url(), "/action.php?action=login&code=2")
        self.assertEqual(http.body, "username=1&pass=223\r\n")
        self.assertEqual(http.state, 6)
        print(http.build())

if __name__ == '__main__':
    unittest.main()
