import json

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items']

        )