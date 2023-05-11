from logging import getLogger
from typing import AnyStr,\
    List
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key

class AccountEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(AccountEndpoints, self).__init__()