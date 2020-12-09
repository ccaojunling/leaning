import json
from datetime import datetime

import requests


class Tag:
    def __init__(self):
        self.token = self.gettoken()

    def gettoken(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={
                             "corpid": "ww913344e2a63b14ac",
                             "corpsecret": "dTm8mcpCCbkRCVv8Cgz4-pFYwstWG_4JGEfderJ14sg"

                         }
                         )
        token =  r.json()["access_token"]
        return token

    def getlist(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params={
                              "access_token": self.token
                          },
                          json={

                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add(self,tag,group_id=None,group_name=None):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={
                              "access_token": self.token
                          },
                          json={
                              "group_id": group_id,
                              "group_name": group_name,
                              "order": 1,
                              "tag": tag
                          }
                          )
        return r

    def update(self,id,name):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params={
                              "access_token": self.token
                          },
                          json={
                              "id": id,
                              "name": name,
                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete(self,group_id,tag_id):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={
                              "access_token": self.token
                          },
                          json={
                              "group_id": group_id,
                              "tag_id": tag_id
                          }
                          )
        return r
