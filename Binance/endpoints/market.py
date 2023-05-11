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