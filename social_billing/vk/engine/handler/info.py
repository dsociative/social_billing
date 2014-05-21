# -*- coding: utf-8 -*-
from social_billing.base_handler import BaseHandler
from social_billing.vk.engine.handler.billing import BillingHandler


class Info(BillingHandler, BaseHandler):

    def __call__(self, item_count):
        name, count = self.split_item_count(item_count)
        good = self.get_good(name)
        return self.response(
            {
                'title': self.title(name, count),
                'price': self.price(good, count),
                'photo_url': self.image(good)
            }
        )
