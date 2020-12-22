import requests


class DingTalkBot(object):

    def __init__(self, token):
        super(DingTalkBot, self).__init__()
        self.url = "https://oapi.dingtalk.com/"
        self.token = token

    def notice(self, message):
        api = "robot/send"
        params = {
            "access_token": self.token,
        }
        data = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        r = requests.post(self.url + api, params=params, json=data)
        print(r.text)
