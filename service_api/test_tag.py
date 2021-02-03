import json
from datetime import datetime

import pytest
import requests

from service_api.tag import Tag


class Testtag:
    def setup_class(self) :
        self.tag = Tag()

    def test_getlist(self):
        r = self.tag.getlist()
        print(r)

    @pytest.mark.parametrize("group_name, tag_id, tag_name", [["测试1组", "etsL6FEAAAtXsOxhkA6yjwY2gjQmjDWg", "tag_1"],
                                                             ["客户等级", "etsL6FEAAA99-sMj_IOTmkGCw7ehGOnQ", " 一般@#"],
                                                             ["客户等级", "etsL6FEAAAsghG9xnkU5V5OYCDhXJwlA", "重要 重要"]])
    def test_tag_update(self, group_name, tag_id, tag_name):
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

    # 40071:标签已经存在
    def test_tag_add(self):
        # todo: 数据放到数据文件里
        tag_name = [{"name":"tag_12"}, {"name":"tag_13"}]
        group_name = "python1"
        r = self.tag.add(tag_name,group_name=group_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        r = self.tag.getlist()
        for i in tag_name:
            tags = [tag for group in r.json()["tag_group"] if group["group_name"] == group_name for tag in group["tag"] if
                    tag["name"] == i["name"]]
            assert tags != []

    def test_tag_delete(self):
        # 40068  无效的tagid，tagid已经被删除了
        group_id = ['etsL6FEAAAfcowgX7XcmTmR8BPU_3I5A']
        tag_id = ['etsL6FEAAApczRS6Ccltn-25Y58qvrRw']
        r = self.tag.delete(group_id,tag_id)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        r = self.tag.getlist()
        for i in tag_id:
            tags = [tag for group in r.json()["tag_group"] if group["group_id"] == group_id for tag in group["tag"] if
                    tag["id"] == i ]
            assert tags == []

    def test_1(self):
        tag_name = [{"name":"tag_12"}, {"name":"tag_13"}]
        a = self.tag.before_add(tag = tag_name,group_name="123")
        print (a)
