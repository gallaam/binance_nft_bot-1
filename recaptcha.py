from settings import BINANCE_SITEKEY

from twocaptcha import TwoCaptcha


def resolve_captcha(product_id: str) -> str:
    """result: dict = {'captchaId': '12345678', 'code': '03dAf...'}"""

    # your own API KEY from https://2captcha.com/enterpage
    solver = TwoCaptcha(apiKey='')
    url = 'https://www.binance.com/en/nft/blindBox/detail?productId='

    result = solver.recaptcha(
        sitekey=BINANCE_SITEKEY,
        url=url + product_id,
        version='v3',
        score='0.3'
    )
    code = result['code']
    return code
