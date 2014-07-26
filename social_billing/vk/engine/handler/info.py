# -*- coding: utf-8 -*-
from social_billing.base_handler import BaseHandler
from social_billing.vk.engine.handler.billing import BillingHandler


class Info(BillingHandler, BaseHandler):

    def __call__(self, name, item_id):
        good = self.get_good(name)
        return self.response(
            {
                'title': self.title(name, item_id),
                'price': self.price(good, item_id),
                'photo_url': self.image(good, item_id)
            }
        )
