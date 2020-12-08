import json
from datetime import datetime

import pytest
import requests

from service_api.tag import Tag

class  TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("group_name, tag_id, tag_name", [["测试1组", "etsL6FEAAAtXsOxhkA6yjwY2gjQmjDWg", "tag_11"],
                                                             ["客户等级", "etsL6FEAAA99-sMj_IOTmkGCw7ehGOnQ", " 一般!@#"],
                                                             ["客户等级", "etsL6FEAAAsghG9xnkU5V5OYCDhXJwlA", "重要  重要"]])
    def test_tag_list(self, group_name, tag_id, tag_name):
        # group_name = "测试1组"
        # tag_id = "etsL6FEAAAtXsOxhkA6yjwY2gjQmjDWg"
        # tag_name = "自动化名字_"+str(datetime.now().strftime("%Y%m%d%H%M%S"))
        r = self.tag.getlist()
        r = self.tag.update(tag_id,tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        r = self.tag.getlist()
        tags = [tag for group in r.json()["tag_group"] if group["group_name"] == group_name for tag in group["tag"] if tag["name"] == tag_name]
        assert tags !=[]

    def test_tag_add(self):
        tag_name = [{"name":"tag_11"}, {"name":"tag_21"}]
        group_name = "python151"
        r = self.tag.add(tag_name,group_name=group_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        r = self.tag.getlist()
        for i in tag_name:
            tags = [tag for group in r.json()["tag_group"] if group["group_name"] == group_name for tag in group["tag"] if
                    tag["name"] == i["name"]]
            assert tags != []
