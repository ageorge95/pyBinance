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