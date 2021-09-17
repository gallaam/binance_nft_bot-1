import requests

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
