import sys
import threading
import time

from datetime import datetime, timedelta

import requests

from recaptcha import resolve_captcha
from settings import PROXY, headers

COUNT_REQUESTS = 30
# ToDo: delete global variable
captcha_results = list()


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

# ToDo: make decorator with resolve_captcha
def wrapped_captcha(product_id, captcha_results):
    captcha = resolve_captcha(product_id)
    captcha_results.append(captcha)

def prepare_captcha(product_id):
    threads = [None] * COUNT_REQUESTS

    for i in range(len(threads)):
        threads[i] = threading.Thread(
            target=wrapped_captcha,
            args=(product_id, captcha_results),
        )
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    return captcha_results

def send_requests_to_buy(box, start_sale_time: datetime, product_id: str):
    threads = list()
    while True:
        current_time = datetime.today()
        if start_sale_time <= (current_time + timedelta(seconds=30)):
            print('Prepare captcha')
            captcha_list = prepare_captcha(product_id)
            print('Prepare completed')
            break

    while True:
        current_time = datetime.today()
        if start_sale_time <= (current_time + timedelta(seconds=1)):
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
