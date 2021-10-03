import sys
import threading
import time
from datetime import datetime, timedelta

import requests

from settings import PROXY, headers


def event_is_not_over(status: int) -> bool:
    return status == 0

def headers_is_right() -> bool:
    user_info = 'https://www.binance.com/bapi/accounts/v1/private/account/user/base-detail'
    response = requests.post(user_info, headers=headers)

    if response.status_code == 200:
        print('Successfully connected\n')
        return True
    else:
        print('Something wrong...')
        print('Check please: COOKIE, CSRFTOKEN, headers')
        return False

# ToDo: refactoring
def send_requests_to_buy(box, start_sale_time: datetime):
    threads = list()
    while True:
        current_time = datetime.today()
        if start_sale_time <= (current_time + timedelta(seconds=12)):
            for _ in range(1, 10000):
                request = threading.Thread(
                    target=box._buy_box,
                    args=(PROXY,)
                )
                request.start()
                threads.append(request)
                time.sleep(0.13)

                if start_sale_time <= (current_time - timedelta(seconds=3)):
                    print('The sale is over!')
                    sys.exit(0)

            for thread in threads:
                thread.join()
