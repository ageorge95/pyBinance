from Binance.logger import configure_logger
from Binance.pyBinance import pyBinance
from pprint import pprint
from os import getenv

if __name__ == '__main__':
    configure_logger()
    # ########### general examples ###########
    # initialize the APi wrapper
    API_obj = pyBinance()

    # test connectivity
    # pprint(API_obj.test_connectivity())
