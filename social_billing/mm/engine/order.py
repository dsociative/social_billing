# -*- coding: utf8 -*-
from social_billing.base_order import BaseOrder


class MMOrder(BaseOrder):

    def __call__(self, uid, transaction_id, item, item_id):
        if not self.has_order(transaction_id):
            self.process(
                transaction_id, uid, item, item_id
            )
        return {'status': 1}