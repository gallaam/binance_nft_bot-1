import json

from typing import Dict


class Headers:
    user_agent: str = 'Mozilla/5.0 (X11; Linux x86_64)' # Your own user-agent
    clienttype: str = 'web'
    cookie: str = 'COOKIE'.encode('utf-8')
    csrftoken: str = 'CSRFTOKEN'
    content_type: str = 'application/json'


class Body:
    productId: str
    number: int # Amount of boxes


class BaseRequest:
    url: str


class RequestBoxInfo(BaseRequest):
    product_id: str


class RequestBoxBuy(BaseRequest):
    headers: dict
    json: Dict[str, json.dumps(dict())]
