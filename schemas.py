import json


class Headers:
    user_agent: str
    clienttype: str
    cookie: str
    csrftoken: str
    content_type: str


class Body:
    productId: str
    number: int # Amount of boxes


class BaseRequest:
    url: str


class RequestBoxInfo(BaseRequest):
    product_id: str


class RequestBoxBuy(BaseRequest):
    headers: dict
    data: json.dumps(dict())
