# https://lbs.amap.com/api/webservice/summary


class Gaode(object):

    url = "https://restapi.amap.com/"

    def __init__(self, key):
        self.key = key
        self.s = requests.Session()

    def driving(self, origin, dest):
        api = "v3/direction/driving"
        params = {
            "key": self.key,
            "origin": origin,
            "destination": dest,
            "output": "json",
            "extensions": "base"
        }
        r = self.s.get(self.url + api, params=params)
        data = r.json()
        return data
