import json

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data_new1 = json_travel(data, 1, 1, 2)
        flow.response.text = json.dumps(data_new1)


# 修改的数据类型：字典，列表，字符串，数字，可以进行
def json_travel(data, array=None, text=1, num=1, key=None):
    """
    :param data: 传入要修改的数据
    :param array: 列表数据修改规则，传入None，不修改
    :param text: 字符串数据修改规则，传1，不修改
    :param num: 数字类型数据修改，传1，不修改
    :return:
    """
    data_new = None
    # 判断传入的数据类型是不是字典
    if isinstance(data, dict):
        data_new = dict()
        # 对字典里的每个结果进行操作
        for k, v in data.items():
            data_new[k] = json_travel(v, array, text, num, k)
    # 对列表数据进行操作
    elif isinstance(data, list):
        data_new = list()
        # 遍历列表中的每个数据
        for item in data:
            item_new = json_travel(item, array, text, num)
            # 传入的array为None，则不做处理，直接返回
            if array is None:
                data_new.append(item_new)
            else:
                # 传入的加倍值是正整数
                if isinstance(array, int) and array >= 0:
                    # 做加倍拼接
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    # 传入的加倍值不是正整数，无法操作，直接返回
                    data_new = data
    # 对字符串进行操作
    elif isinstance(data, str):
        # 加倍参数是正整数，则做加倍操作
        if isinstance(text, int) and text >= 0:
           # import ipdb;ipdb.set_trace()
           # data_new = data * text
            if key == 'name':
                data_new = data * 2
            else:
                data_new = data

        # 加倍参数不符合规则，则不做操作
        else:
            data_new = data
    # 对数字进行操作
    elif isinstance(data, int) or isinstance(data, float):
        # 输入的数字的规则为数字
        if isinstance(num, int) or isinstance(num, float):
            data_new = data * num
        # 不为数字，则直接返回
        else:
            data_new = data
    # 其他条件，直接返回
    else:
        data_new = data
    # 返回处理后的结果
    return data_new
