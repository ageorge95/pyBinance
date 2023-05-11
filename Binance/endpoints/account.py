from logging import getLogger
from typing import AnyStr,\
    List
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key
from urllib.parse import urlencode
from hashlib import sha256
from hmac import digest
from datetime import datetime
from requests import delete

class AccountEndpoints():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr
    API_secret : AnyStr

    def __init__(self):
        super(AccountEndpoints, self).__init__()

    @check_API_key
    def current_open_orders(self,
                            symbol: AnyStr,
                            max_retries: int = 1):
        added_url = r'api/v3/openOrders'

        data={'symbol': symbol,
              'timestamp': int(datetime.now().timestamp()*1000)}
        queryString = urlencode(data)
        signature = digest(self.API_secret.encode('utf-8'),
                           queryString.encode('utf-8'),
                           sha256).hex()
        data['signature'] = signature

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def all_orders(self,
                   symbol: AnyStr,
                   limit: int = 5,
                   max_retries: int = 1):
        added_url = r'api/v3/allOrders'

        data = {'symbol': symbol,
                'limit': limit,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        queryString = urlencode(data)
        signature = digest(self.API_secret.encode('utf-8'),
                           queryString.encode('utf-8'),
                           sha256).hex()
        data['signature'] = signature

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def query_order(self,
                    symbol: AnyStr,
                    orderId: int,
                    max_retries: int = 1):
        added_url = r'api/v3/order'

        data = {'symbol': symbol,
                'orderId': orderId,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        queryString = urlencode(data)
        signature = digest(self.API_secret.encode('utf-8'),
                           queryString.encode('utf-8'),
                           sha256).hex()
        data['signature'] = signature

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def cancel_order(self,
                     symbol: AnyStr,
                     orderId: int,
                     max_retries: int = 1):
        added_url = r'api/v3/order'

        data = {'symbol': symbol,
                'orderId': orderId,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        queryString = urlencode(data)
        signature = digest(self.API_secret.encode('utf-8'),
                           queryString.encode('utf-8'),
                           sha256).hex()
        data['signature'] = signature

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries,
                        call_method=delete).send()