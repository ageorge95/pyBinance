from logging import getLogger
from typing import AnyStr
from Binance.endpoints.market import MarketEndpoints
from Binance.endpoints.general import GeneralEndpoints
from Binance.endpoints.account import AccountEndpoints
from Binance.endpoints.simple_earn import SimpleEarn

base_endpoint: AnyStr = 'https://api3.binance.com'

class pyBinance(MarketEndpoints,
                GeneralEndpoints,
                AccountEndpoints,
                SimpleEarn):

    def __init__(self,
                 API_key: AnyStr = None,
                 API_secret: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key
        self.API_secret = API_secret

        self.base_endpoint = base_endpoint

        super(pyBinance, self).__init__()
