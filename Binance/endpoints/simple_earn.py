from logging import getLogger
from typing import AnyStr
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key,\
    hmac_signature
from datetime import datetime
from requests import delete,\
    post

class SimpleEarn():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr
    API_secret : AnyStr

    def __init__(self):
        super(SimpleEarn, self).__init__()

    @check_API_key
    def simple_earn_products(self,
                             max_retries: int = 1):
        added_url = r'sapi/v1/simple-earn/flexible/list'

        data={'timestamp': int(datetime.now().timestamp()*1000)}
        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()