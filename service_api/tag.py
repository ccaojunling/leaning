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

    def add(self,tag,group_id=None,group_name=None,**kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id,
                "group_name": group_name,
                "order": 1,
                "tag": tag,
                **kwargs
            }
        }
        r = self.send(data)
        return r

    def before_add(self,tag,group_id=None,group_name=None,**kwargs):
        r = self.add(tag,group_id,group_name,**kwargs)
        print(r.status_code)
        print(r.json()["errcode"])
        if r.status_code == 200 and r.json()["errcode"] == 40071:
            for group  in self.getlist().json()["tag_group"]:
                print ("-----------")
                print(group)
                if group_name not in group:
                    print ("group name not in group")
                    return False

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

    def delete_tag(self,tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id
            }
        }
        r = self.send(data)
        return r

    def delete_group(self,group_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id
            }
        }
        r = self.send(data)
        return r


if __name__ == '__main__':
    tag = Tag()
    a = tag.before_add(tag= "11111", group_name="123")
    print (a)


