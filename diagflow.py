import os
from urllib.parse import urlencode

import requests

BEARER = os.getenv('BEARER_KEY')


def get_url():
    print(BEARER)
    params = urlencode(dict(v=20150910))
    url = 'https://api.dialogflow.com/v1/query?{0}'.format(params)
    return requests.get(url, headers={'Authorization': BEARER})


print(get_url())
