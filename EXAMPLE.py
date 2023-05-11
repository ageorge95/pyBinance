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
    # API_obj = pyBinance()

    # orderbook
    # pprint(API_obj.order_book(symbol='BTCUSDT'))
    # pprint(API_obj.order_book(symbol='BTCUSDT', limit=5))

    # symbol price ticker
    # pprint(API_obj.symbol_price_ticker(symbol='BTCUSDT'))
    # pprint(API_obj.symbol_price_ticker(symbol=['BTCUSDT','ETHUSDT']))

    # ########### account examples ###########
    # initialize the APi wrapper
    API_obj = pyBinance(API_key=getenv('BINANCE_API_KEY'),
                        API_secret=getenv('BINANCE_API_SECRET'))

    # current open orders
    # pprint(API_obj.current_open_orders(symbol='ARPABUSD'))

    # all_orders
    # pprint(API_obj.all_orders(symbol='ARPABUSD'))

    # query order
    # pprint(API_obj.query_order(symbol='ARPABUSD',
    #                            orderId=122907817))

    # cancel order
    # pprint(API_obj.cancel_order(symbol='ARPABUSD',
    #                             orderId=122907817))