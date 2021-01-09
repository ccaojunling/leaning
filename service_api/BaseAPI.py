import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.gettoken()

    def gettoken(self):

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": "ww913344e2a63b14ac",
                      "corpsecret": "dTm8mcpCCbkRCVv8Cgz4-pFYwstWG_4JGEfderJ14sg"}

        }
        r = self.send(data)

        access_token = r.json()["access_token"]
        return access_token

    def send(self,kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r