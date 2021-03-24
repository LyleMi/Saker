import json
import requests


class Whois(object):

    url = "https://api.devopsclub.cn/api/whoisquery"

    def __init__(self):
        super(Whois, self).__init__()
        self.s = requests.Session()

    def domainReport(self, domain):
        params = {
            "domain": domain,
            "type": "json"
        }
        r = self.s.get(self.url, params=params)
        try:
            data = json.loads(r.text)
            data = data['data']
        except Exception as e:
            # ban by cf
            print(repr(e))
            data = []
        return data
