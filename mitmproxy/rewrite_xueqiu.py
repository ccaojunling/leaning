import json

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][1]['quote']['name']= ""
        flow.response.text = json.dumps(data)

def json_travel(data,array,text,num):
    """

    :param data: 传入要修改的数据
    :param array:
    :param text:
    :param num:
    :return:
    """