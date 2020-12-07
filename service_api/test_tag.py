import json

import requests


def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                     params={
                         "corpid": "ww913344e2a63b14ac",
                         "corpsecret":"dTm8mcpCCbkRCVv8Cgz4-pFYwstWG_4JGEfderJ14sg"

                     }
    )
    return r.json()["access_token"]


def test_tag_list():
    ACCESS_TOKEN = get_token()
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                      params={
                          "access_token": ACCESS_TOKEN
                      },
                      json={

                      }
      )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

def test_edit_tag():
    ACCESS_TOKEN = get_token()
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                      params={
                          "access_token": ACCESS_TOKEN
                      },
                      json={
                          "id": "etsL6FEAAAtXsOxhkA6yjwY2gjQmjDWg",
                          "name": "标签999",
                      }
                      )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0
