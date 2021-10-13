import threading
from twocaptcha import TwoCaptcha

from settings import BINANCE_SITEKEY, CAPTCHA_API_KEY, COUNT_REQUESTS


class Recaptcha:

    def __init__(self, product_id: str):
        self.captcha_results = list()
        self.product_id = product_id

    def resolve_captcha(self) -> str:
        """result: dict = {'captchaId': '12345678', 'code': '03dAf...'}"""

        # your own API KEY from https://2captcha.com/enterpage
        solver = TwoCaptcha(apiKey=CAPTCHA_API_KEY)
        url = 'https://www.binance.com/en/nft/goods/detail?productId='

        result = solver.recaptcha(
            sitekey=BINANCE_SITEKEY,
            url=url + str(self.product_id),
            version='v3',
            score='0.3'
        )
        code = result['code']
        return code

    def wrapped_captcha(self) -> None:
        captcha = self.resolve_captcha()
        self.captcha_results.append(captcha)

    def prepare_captcha(self) -> list:
        threads = [None] * COUNT_REQUESTS

        for i in range(len(threads)):
            threads[i] = threading.Thread(
                target=self.wrapped_captcha,
            )
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()

        return self.captcha_results
