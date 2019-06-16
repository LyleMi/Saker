
import zlib
import json

from itsdangerous import base64_decode, base64_encode

from flask import Flask
from flask.sessions import SecureCookieSessionInterface


class FlaskEncoder(object):

    salt = "cookie-session"

    def __init__(self, secret_key=None):
        self.compressed = False
        if secret_key is None:
            self.session_serializer = None
        else:
            app = Flask(__name__)
            app.secret_key = secret_key
            self.session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

    def decode(self, cookie):
        if self.session_serializer is None:
            payload = cookie
            if payload.startswith('.'):
                self.compressed = True
                payload = payload[1:]
            data = payload.split(".")[0]
            data = base64_decode(data)
            if self.compressed:
                data = zlib.decompress(data)
            return json.loads(data.decode("utf-8"))
        else:
            return self.session_serializer.loads(cookie)

    def encode(self, cookie, secret_key=None):
        if self.session_serializer is None:
            if self.compressed:
                cookie = "." + base64_encode(zlib.compress(cookie))
            else:
                cookie = base64_encode(cookie)
            return cookie
        else:
            return self.session_serializer.dumps(cookie)
