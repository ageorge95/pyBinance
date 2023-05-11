from logging import getLogger
from typing import AnyStr
from Binance.endpoints.market import MarketEndpoints
from Binance.endpoints.general import GeneralEndpoints
from Binance.endpoints.account import AccountEndpoints

base_endpoint: AnyStr = 'https://api3.binance.com'

class pyBinance(MarketEndpoints,
                GeneralEndpoints,
                AccountEndpoints):

    def __init__(self,
                 API_key: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key

        self.base_endpoint = base_endpoint

        super(pyBinance, self).__init__()
