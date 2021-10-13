import sys
import threading
import time

from datetime import datetime, timedelta

import requests

from recaptcha import Recaptcha
from settings import COUNT_REQUESTS, PROXY, headers


def event_is_not_over(status: int) -> bool:
    return status == 0

def headers_is_right() -> bool:
    user_info = 'https://www.binance.com/bapi/accounts/v1/private/account/user/base-detail'
    response = requests.post(user_info, headers=headers)

    if response.status_code == 200:
        print('Successfully connected\n')
    else:
        print('Something wrong...')
        print('Check please: COOKIE, CSRFTOKEN, headers')
        sys.exit(1)

def send_requests_to_buy(box, start_sale_time: datetime, product_id: str):
    threads = list()
    captcha = Recaptcha(product_id)

    while True:
        current_time = datetime.today()
        if start_sale_time <= (current_time + timedelta(seconds=105)):
            print('Prepare captcha')
            captcha_list = captcha.prepare_captcha()
            print('Prepare completed')
            break

    while True:
        current_time = datetime.today()
        if start_sale_time <= (current_time + timedelta(seconds=1.5)):
            print('Start sale')
            for _ in range(0, COUNT_REQUESTS):
                request = threading.Thread(
                    target=box._buy_box,
                    args=(PROXY, captcha_list.pop())
                )
                request.start()
                threads.append(request)
                time.sleep(0.15)

            for thread in threads:
                thread.join()

            print('Sale has been ended')
            sys.exit(0)
