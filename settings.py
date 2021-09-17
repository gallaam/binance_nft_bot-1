CSRFTOKEN = ''
COOKIE = ''

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)',
    'clienttype': 'web',
    'cookie': COOKIE.encode('utf-8'),
    'csrftoken': CSRFTOKEN,
    'content-type': 'application/json'
}