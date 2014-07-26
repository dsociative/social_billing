# -*- coding: utf8 -*-
from social_billing.vk.engine.errors import UnknownItemError, InvalidCountError


class BaseHandler(object):
    def __init__(self, goods):
        self.goods = goods

    def get_good(self, name):
        item = self.goods.get(name)
        if item is None:
            raise UnknownItemError()
        return item

    def get_item(self, good, item_id):
        item = good.get(item_id)

        if item is None:
            raise InvalidCountError()
        else:
            return item

    def price(self, good, item_id):
        return self.get_item(good, item_id)['price']

    def title(self, name, item_id):
        return self.get_item(self.get_good(name), item_id)['title']

    def image(self, good, item_id):
        return self.get_item(good, item_id).get('image', '')