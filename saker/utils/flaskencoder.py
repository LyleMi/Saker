
import zlib
import json
import hashlib
from itsdangerous import base64_decode, base64_encode
from itsdangerous import URLSafeTimedSerializer
from flask.json.tag import TaggedJSONSerializer

session_json_serializer = TaggedJSONSerializer()

class FlaskEncoder(object):

    salt = "cookie-session"
    key_derivation = "hmac"
    digest_method = staticmethod(hashlib.sha1)
    serializer = session_json_serializer

    def __init__(self):
        self.compressed = False

    def decode(self, cookie):
        payload = cookie
        if payload.startswith('.'):
            self.compressed = True
            payload = payload[1:]
        data = payload.split(".")[0]
        data = base64_decode(data)
        if self.compressed:
            data = zlib.decompress(data)
        return json.loads(data.decode("utf-8"))

    def encode(self, cookie, secret_key=None):
        if secret_key is None:
            if self.compressed:
                cookie = "." + base64_encode(zlib.compress(cookie))
            else:
                cookie = base64_encode(cookie)
            return cookie
        signer_kwargs = dict(
            key_derivation=self.key_derivation, digest_method=self.digest_method
        )
        serializer = URLSafeTimedSerializer(
            secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs,
        )
        return serializer.dumps(cookie)

