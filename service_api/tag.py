import json
from datetime import datetime

import requests

from service_api.BaseAPI import BaseApi


class Tag(BaseApi):

    def getlist(self):
        data = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params":{"access_token": self.token}
        }
        r = self.send(data)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add(self,tag,group_id=None,group_name=None):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id,
                "group_name": group_name,
                "order": 1,
                "tag": tag
            }
        }
        r = self.send(data)
        return r
    #add 如果已经存在的标签，要先删除再添加
    def add_and_detect(self):
        pass


    def update(self,id,name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "id": id,
                "name": name
            }
        }
        r = self.send(data)
        return r

    def delete(self,group_id,tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id,
                "tag_id": tag_id
            }
        }
        r = self.send(data)
        return r
