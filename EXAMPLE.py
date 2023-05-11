from Binance.logger import configure_logger
from Binance.pyBinance import pyBinance
from pprint import pprint
from os import getenv

if __name__ == '__main__':
    configure_logger()
    # ########### general examples ###########
    # initialize the APi wrapper
    # API_obj = pyBinance()

    # test connectivity
    # pprint(API_obj.test_connectivity())

    # check server time
    # pprint(API_obj.check_server_time())

    # exchange information
    # pprint(API_obj.exchange_information(symbol='BTCUSDT'))
    # pprint(API_obj.exchange_information(symbol=['BTCUSDT','ETHUSDT']))

    # ########### market examples ###########
    # initialize the APi wrapper
    API_obj = pyBinance()

    # orderbook
    # pprint(API_obj.order_book(symbol='BTCUSDT'))
    # pprint(API_obj.order_book(symbol='BTCUSDT', limit=5))