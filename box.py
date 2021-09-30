import json
from abc import abstractmethod
from collections import defaultdict
from datetime import datetime
from typing import Optional, Union

import requests

from recaptcha import resolve_captcha
from handlers import event_is_not_over
from schemas import Body, Headers
from settings import headers


class BaseBox:

    def __init__(self):
        self._box_list = 'https://www.binance.com/bapi/nft/v1/public/nft/mystery-box/list?page=1&size=15'
    
    def get_list_boxes(self) -> dict:
        return requests.get(self._box_list).json()['data']

    def get_avalible_boxes(self) -> dict:
        avalible_boxes = defaultdict(dict)
        boxes = self.get_list_boxes()
        box_num = 0

        for box in boxes:
            status = box['status']
            name = box['name']
            product_id = box['productId']

            if event_is_not_over(status):
                box_num += 1
                avalible_boxes[str(box_num)] = {
                    'name': name,
                    'product_id': product_id
                }
        
        return avalible_boxes
    
    @staticmethod
    def log_info_boxes(avalible_boxes: dict) -> None:
        for box_num, value in avalible_boxes.items():
            print(f'{box_num}. {value["name"]}')


class Box(BaseBox):

    def __init__(
        self,
        amount: int=0,
        product_id: Optional[Union[str, int]]='',
    ):
        super().__init__()
        self._box_info: str = 'https://www.binance.com/bapi/nft/v1/friendly/nft/mystery-box/detail?productId='
        self._box_buy: str = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'

        self._product_id = product_id
        self._amount = amount

        self._headers: dict = headers
        self._body: Body = {
            'productId': product_id,
            'number': amount
        }

    @property
    @abstractmethod
    def _get_box_info(self) -> dict():
        return requests.get(self._box_info + str(self._product_id)).json()['data']

    @property
    @abstractmethod
    def _get_start_sale_time(self) -> datetime:
        start_sale = self._get_box_info['startTime']
        start_sale_time = datetime.fromtimestamp(start_sale/1000)
        return start_sale_time

    @abstractmethod
    def _buy_box(self, proxy) -> json:
        # resolve invisible recaptcha V3
        self._headers['x-nft-checkbot-token'] = resolve_captcha(self._product_id)

        response = requests.post(
            self._box_buy, headers=self._headers,
            data=json.dumps(self._body),
            proxies={'http': f'http://{proxy}/'}
        )
        print(response.json())
        return response
