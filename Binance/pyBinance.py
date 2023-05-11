from logging import getLogger
from typing import AnyStr
from Binance.wallet import PublicWallet,\
    PrivateWallet
from Binance.spot import PublicSpot,\
    PrivateSpot

base_endpoint: AnyStr = 'https://api3.binance.com'

class pyBinance(PublicWallet,
                PrivateWallet,
                PublicSpot,
                PrivateSpot):

    def __init__(self,
                 API_key: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key

        self.base_endpoint = base_endpoint

        super(pyBinance, self).__init__()

