from logging import getLogger
from typing import AnyStr,\
    List
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key

class MarketEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(MarketEndpoints, self).__init__()

    def order_book(self,
                   symbol: AnyStr,
                   limit: int = 20,
                   max_retries: int = 1):

        added_url = r'api/v3/depth'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={'symbol': symbol,
                              'limit': limit},
                        max_retries=max_retries).send()
