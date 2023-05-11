from logging import getLogger
from typing import AnyStr,\
    List
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key

class PublicWallet():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicWallet, self).__init__()

class PrivateWallet():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr

    def __init__(self):
        super(PrivateWallet, self).__init__()