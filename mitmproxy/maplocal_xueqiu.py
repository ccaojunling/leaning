from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url:
        with open("D:\\quote.json",encoding='UTF-8') as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(), # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
        )