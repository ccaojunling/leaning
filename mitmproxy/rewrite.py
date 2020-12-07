import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 获取到要修改数据的名字
        new_name = data['data']['items'][1]['quote']['name']
        # 进行加倍显示
        data['data']['items'][1]['quote']['name'] = new_name * 2
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)