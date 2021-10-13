COUNT_REQUESTS = 15

# Give it here - https://2captcha.com/enterpage
CAPTCHA_API_KEY = ''

BINANCE_SITEKEY = '6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_'

# Yours own proxy here `username:password@ip:port` [NOT REQUIRE]
PROXY = ''

CSRFTOKEN = ''
COOKIE = ''

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "bnc-uuid": "",
    "clienttype": "web",
    "content-type": "application/json",
    "cookie": COOKIE.encode("UTF-8"),
    "csrftoken": CSRFTOKEN,
    "device-info": "",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "lang": "en",
    "x-nft-checkbot-sitekey": BINANCE_SITEKEY,
}