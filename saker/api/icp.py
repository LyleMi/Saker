import json
import requests


class ICP(object):

    url = "https://api.devopsclub.cn/api/icpquery"

    def __init__(self):
        super(ICP, self).__init__()
        self.s = requests.Session()

    def icp(self, domain):
        params = {
            "url": domain,
        }
        r = self.s.get(self.url, params=params)
        try:
            data = json.loads(r.text)
            # print(data)
            if data['code'] == 1:
                # error occur
                return data
            data = data["data"]
        except Exception as e:
            # ban by cf
            print(repr(e))
            data = []
        return data
