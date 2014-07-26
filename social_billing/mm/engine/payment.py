# -*- coding: utf8 -*-
from social_billing.base_handler import BaseHandler
from social_billing.base_payment import BasePayment
from social_billing.core import BillingCore
from social_billing.mm.engine.order import MMOrder
from social_billing.vk.engine.errors import SignatureError, InvalidCountError
from social_billing.vk.engine.signature import Signature


class MMPayment(BaseHandler, BasePayment):
    COUNT_FIELD = 'service_id'
    PRICE_FIELD = 'mailiki_price'

    def __init__(self, name, goods, secret, callback):
        BaseHandler.__init__(self, goods)
        BasePayment.__init__(self, goods)

        self.signature = Signature(secret)
        self.callback = callback
        self.order = MMOrder(name, callback)

    def check_price(self, name, item_id, price):
        if self.price(self.get_good(name), item_id) != price:
            raise InvalidCountError

    def request(self, args):
        try:
            self.signature.try_check(args)
            item_id, name, count = self.get_name_count(args[self.COUNT_FIELD])
            price = int(args[self.PRICE_FIELD])
            self.check_price(name, item_id, price)
            return self.order(args['uid'], args['transaction_id'], name,
                              count)
        except SignatureError:
            return {'status': 0, 'error_code': 700}
        except InvalidCountError:
            return {'status': 0, 'error_code': 703}
