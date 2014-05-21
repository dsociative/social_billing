# -*- coding: utf8 -*-
from social_billing.base_handler import BaseHandler
from social_billing.core import BillingCore
from social_billing.mm.engine.order import MMOrder
from social_billing.vk.engine.errors import SignatureError, InvalidCountError
from social_billing.vk.engine.signature import Signature


class MMPayment(BaseHandler):
    COUNT_FIELD = 'service_id'
    PRICE_FIELD = 'mailiki_price'

    def __init__(self, name, goods, secret, callback):
        super(MMPayment, self).__init__(goods)
        self.signature = Signature(secret)
        self.callback = callback
        self.order = MMOrder(name, callback)
        self.item = BillingCore.default_item

    def check_price(self, count, price):
        if self.price(self.get_good(self.item), count) != price:
            raise InvalidCountError

    def request(self, args):
        try:
            self.signature.try_check(args)
            count = int(args[self.COUNT_FIELD])
            price = int(args[self.PRICE_FIELD])
            self.check_price(count, price)
            return self.order(args['uid'], args['transaction_id'], self.item,
                              count)
        except SignatureError:
            return {'status': 0, 'error_code': 700}
        except InvalidCountError:
            return {'status': 0, 'error_code': 703}
