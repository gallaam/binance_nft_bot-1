import requests
from datetime import datetime

from settings import headers
from user.urls import user_info


def event_is_not_over(status: int) -> bool:
    return status == 0

def headers_is_right() -> bool:
    response = requests.post(user_info, headers=headers)

    if response.status_code == 200:
        print('Successfully connected')
        return True
    else:
        print('Something wrong...')
        print('Check please: COOKIE, CSRFTOKEN, headers')
        return False

def send_requests_to_buy(box, start_sale_time: datetime):
    while True:
        current_time = datetime.today()

        if start_sale_time >= current_time:
            print('Start buying')
            while True:
                response = box._buy_box
                print(response)
