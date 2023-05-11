from logging import getLogger
from typing import AnyStr,\
    Literal
from time import sleep
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key,\
    full_nr_normalisation

class PublicSpot():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicSpot, self).__init__()

class PrivateSpot():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr

    def __init__(self):
        super(PrivateSpot, self).__init__()