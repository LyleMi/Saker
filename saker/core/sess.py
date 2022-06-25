import os
import json
import pickle
import random
import requests

from saker.handler.headerHandler import HeaderHandler
from saker.utils.url import normalizeUrl
from saker.utils.hash import md5
from saker.utils.logger import getLogger
from saker.utils.datatype import AttribDict
from saker.utils.paths import Paths


class Sess(object):

    """Core Scanner

    Attributes:
        ffua (str): Firefox User Agent Str for default UA
        jsonr (TYPE): JSON response
        lastr (TYPE): last response
        s (TYPE): Session
        timeout (int): Default requests timeout
        url (TYPE): Main url
    """

    # 'Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>'
    ffua = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:95.0) Gecko/20100101 Firefox/95.0'

    def __init__(
            self, url="", verify=False,
            timeout=0, loglevel="debug"
    ):
        """
        Args:
            url (str, optional): main url
            verify (bool, optional): verify or not
            timeout (int, optional): requests timeout
        """
        super(Sess, self).__init__()
        self.s = requests.Session()
        if timeout != 0:
            self.timeout = timeout
        self.url = normalizeUrl(url)
        self.loglevel = loglevel
        self.logger = getLogger()
        self.lastr = None
        self.s.verify = verify
        self.setUA(self.ffua)

    def get(self, path="", *args, **kwargs):
        self.lastr = self.s.get(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def post(self, path="", *args, **kwargs):
        self.lastr = self.s.post(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def put(self, path="", *args, **kwargs):
        self.lastr = self.s.put(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def patch(self, path="", *args, **kwargs):
        self.lastr = self.s.patch(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def delete(self, path="", *args, **kwargs):
        self.lastr = self.s.delete(self.url + path, *args, **kwargs)
        self._callback()
        return self.lastr

    def cacheGet(self, path="", cachefile=None):
        if cachefile is None:
            cachefile = '.%s.html' % md5(path)
        if os.path.exists(cachefile):
            self.logger.debug('cache %s hit' % path)
            with open(cachefile, 'rb') as fh:
                return fh.read()
        else:
            self.get(path)
            self.logger.debug('cache save %s to file %s' % (path, cachefile))
            with open(cachefile, 'wb') as fh:
                fh.write(self.lastr.content)
                return self.lastr.content

    def trace(self):
        """Trace requests
        """
        if self.lastr is None:
            return
        print(self.lastr.request.url)
        print(self.lastr.request.body)
        HeaderHandler(self.lastr.request.headers).show()
        HeaderHandler(self.lastr.headers).show()
        print(self.lastr.text)
        if not self.lastr.history:
            return
        for r in self.lastr.history:
            print(r.url)
        print(self.lastr.url)

    def _callback(self):
        """Request Callback
        """
        if 'Content-Type' in self.lastr.headers and self.lastr.headers['Content-Type'].startswith('application/json;'):
            self.jsonLoadr()

    def jsonLoadr(self):
        """load json response
        """
        if self.lastr is None:
            return
        try:
            self.jsonr = AttribDict(json.loads(self.lastr.text))
            return self.jsonr
        except json.decoder.JSONDecodeError as e:
            pass
        except Exception as e:
            print(repr(e))

    def loadCookie(self, pkl='.cookie.pkl'):
        """load saved cookie

        Args:
            pkl (str, optional): cookie file name
        """
        self.logger.debug('loading cookie...')
        with open(pkl, 'rb') as fh:
            self.s.cookies = pickle.load(fh)

    def saveCookie(self, pkl='.cookie.pkl'):
        """save cookie

        Args:
            pkl (str, optional): cookie file name
        """
        self.logger.debug('save cookie...')
        with open(pkl, 'wb') as fh:
            pickle.dump(self.s.cookies, fh)

    def setCookie(self, key, value, **kwargs):
        self.s.cookies.set(key, value)

    def setProxies(self, proxies):
        """set request proxies
        """
        if isinstance(proxies, dict):
            self.s.proxies = proxies
        elif isinstance(proxies, str):
            self.s.proxies = {
                "http": proxies,
                "https": proxies,
            }

    def setHeader(self, key, value):
        self.s.headers[key] = value

    def setUA(self, UA=""):
        """set default User Agent
        """
        ua = UA if UA else self.randua()
        self.setHeader("User-Agent", ua)

    def setXFF(self, ip="1.1.1.1", setAll=False):
        commonHeaders = [
            "X-Forwarded-For",
            "X-Real-IP",
            "HTTP_CLIENT_IP",
        ]
        allHeaders = [
            "Ali-CDN-Real-IP",
            "Cdn-Real-Ip",
            "Cdn-Src-Ip",
            "CF-Connecting-IP",
            "Client-IP",
            "Fastly-Client-Ip",
            "Proxy-Client-IP",
            "True-Client-Ip",
            "WL-Proxy-Client-IP",
            "X-Client-IP",
            "X-Cluster-Client-IP",
            "X-Forwarded",
            "X-Forwarded-By",
            "X-Forwarded-For-Original",
            "X-Forwarded-Host",
            "X-remote-addr",
            "X-remote-IP",
        ]
        if setAll:
            headers = commonHeaders + allHeaders
        else:
            headers = commonHeaders
        for header in headers:
            self.setHeader(header, ip)

    def sendRaw(self, method, url):
        '''
        handle url like ../../../
        '''
        s = requests.Session()
        r = requests.Request(method, url)
        r.url = url
        prepared = r.prepare()
        prepared.url = url
        r = s.send(prepared)
        return r

    def dump(self, filepath):
        with open(filepath, "wb") as fh:
            fh.write(self.lastr.content)

    def randua(self):
        with open(Paths.uas) as fp:
            ua = random.choice([i.strip("\n") for i in fp])
        return ua
