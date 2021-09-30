V 1.2
Bot for automated buying boxes on Binance

Resolve recaptcha V3:
1) Registration here > https://2captcha.com?from=12721485
2) Go here -> https://2captcha.com/enterpage and take your own AKI_KEY ![image](https://user-images.githubusercontent.com/84085341/135535026-bcb8ff40-1b39-49bb-b77d-360a4eee9b67.png)

3) Deposit 3$ on your account on https://2captcha.com/
4) Add your own AKI_KEY in `settings.py` (line 2): `CAPTCHA_API_KEY = 'AKI_KEY'`

Settings:
1) In `settings.py` put your own CSRFTOKEN, COOKIE : `CSRFTOKEN = 'csrf here'`, `COOKIE = 'cookie here'`
2) In `settings.py` in `headers` put your `bnc-uuid`, `device-info` and `user-agent`

E.g. go here - https://www.binance.com/en/nft/blindBox/detail?productId=139168165799316480
1) Click on right button on mouse then select `inspect`
2) Then - select `Network` and `Fetch/XHR` ![image](https://user-images.githubusercontent.com/84085341/135534545-e9491094-778b-4dc4-8356-4d6df7705edb.png)
3) Reload page
4) Click on `auth` - ![image](https://user-images.githubusercontent.com/84085341/135534699-2c61de0a-d85f-4c53-bd7a-92a0d30b4b85.png)
5) Take info in `Request Headers` - ![image](https://user-images.githubusercontent.com/84085341/135534810-082668e7-757f-45c7-bb5e-2bdef96549d0.png)

Proxy (IS NOT REQUIRE):
1) username:password@ip_address:port ![image](https://user-images.githubusercontent.com/84085341/135535325-5eb58451-b785-4df3-88e1-a38fcc10b986.png)

Start:
1) `python3 main.py` or `python main.py`
2) If you have error, try: `pip3 install -r requirements.txt`
3) Select box ![image](https://user-images.githubusercontent.com/84085341/135535771-1e285214-c75b-41a6-b6f9-2636c975d0de.png)
4) Select amount ![image](https://user-images.githubusercontent.com/84085341/135535807-9b47834b-f169-47db-bdc5-7fd793f07203.png)

Thats all!

developer: Matvey Semenov

telegram: @matvey_dev

vk: https://vk.com/wannafckingdie
