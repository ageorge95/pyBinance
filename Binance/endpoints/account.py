from logging import getLogger
from typing import AnyStr
from Binance.network_wrappers import API_call
from Binance.utils import check_API_key,\
    hmac_signature
from datetime import datetime
from requests import delete,\
    post

class AccountEndpoints():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr
    API_secret : AnyStr

    def __init__(self):
        super(AccountEndpoints, self).__init__()

    @check_API_key
    def account_information(self,
                            max_retries: int = 1):
        added_url = r'api/v3/account'

        data={'timestamp': int(datetime.now().timestamp()*1000)}
        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def current_open_orders(self,
                            symbol: AnyStr = None,
                            max_retries: int = 1):
        added_url = r'api/v3/openOrders'

        data = {'timestamp': int(datetime.now().timestamp() * 1000)}
        if symbol:
            data |= {'symbol': symbol}

        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def all_orders(self,
                   symbol: AnyStr,
                   limit: int = 5,
                   max_retries: int = 1):
        added_url = r'api/v3/allOrders'

        data = {'symbol': symbol,
                'limit': limit,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def query_order(self,
                    symbol: AnyStr,
                    orderId: int,
                    max_retries: int = 1):
        added_url = r'api/v3/order'

        data = {'symbol': symbol,
                'orderId': orderId,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries).send()

    @check_API_key
    def cancel_order(self,
                     symbol: AnyStr,
                     orderId: int,
                     max_retries: int = 1):
        added_url = r'api/v3/order'

        data = {'symbol': symbol,
                'orderId': orderId,
                'timestamp': int(datetime.now().timestamp() * 1000)}
        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries,
                        call_method=delete).send()

    @check_API_key
    def test_new_order(self,
                       symbol: AnyStr,
                       side: AnyStr,
                       order_type: AnyStr,
                       quantity: float | AnyStr,
                       price: float | AnyStr = None,
                       timeInForce: AnyStr = 'GTC',
                       newOrderRespType: AnyStr = 'ACK',
                       max_retries: int = 1):
        added_url = r'api/v3/order/test'

        data = {'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
                'newOrderRespType': newOrderRespType,
                'timestamp': int(datetime.now().timestamp() * 1000)}

        if order_type not in ['MARKET']:
            if not price:
                raise Exception(f'A {order_type} order was provided without a price !'
                                f' This is only permitted for MARKET orders.')

            data |= {'timeInForce': timeInForce,
                     'price': price}

        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries,
                        call_method=post).send()

    @check_API_key
    def new_order(self,
                  symbol: AnyStr,
                  side: AnyStr,
                  order_type: AnyStr,
                  quantity: float | AnyStr,
                  price: float | AnyStr = None,
                  timeInForce: AnyStr = 'GTC',
                  newOrderRespType: AnyStr = 'ACK',
                  max_retries: int = 1):
        added_url = r'api/v3/order'

        data = {'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
                'newOrderRespType': newOrderRespType,
                'timestamp': int(datetime.now().timestamp() * 1000)}

        if order_type not in ['MARKET']:
            if not price:
                raise Exception(f'A {order_type} order was provided without a price !'
                                f' This is only permitted for MARKET orders.')

            data |= {'timeInForce': timeInForce,
                     'price': price}

        data['signature'] = hmac_signature(data,
                                           self.API_secret)

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers={'X-MBX-APIKEY': self.API_key},
                        max_retries=max_retries,
                        call_method=post).send()