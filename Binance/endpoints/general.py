from logging import getLogger
from typing import AnyStr,\
    Literal
from time import sleep
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key,\
    full_nr_normalisation

class GeneralEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(GeneralEndpoints, self).__init__()

    def test_connectivity(self,
                          max_retries: int = 1):

        added_url = r'api/v3/ping'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={},
                        max_retries=max_retries).send()

    def check_server_time(self,
                          max_retries: int = 1):

        added_url = r'api/v3/time'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={},
                        max_retries=max_retries).send()